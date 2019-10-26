from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions, renderers, viewsets, status

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, action, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response  import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from trelloapp.models import Board, TrelloList, Card
from .serializers import BoardSerializer,TrelloListSerializer, CardSerializer, UserSerializer

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


from .permissions import IsOwnerOrReadOnly

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# @api_view(['GET']) # new
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('users', request=request, format=format),
#         'boards': reverse('boards', request=request, format=format),
#         'lists': reverse('lists', request=request, format=format),
#         'cards': reverse('cards', request=request, format=format)
#     })


# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def view(request, format=None):
#     content = {
#         'user': unicode(request.user),
#         'auth': unicode(request.auth)
#     }
#     return Response(content)



class BoardViewSet(viewsets.ViewSet, APIView):

    
    queryset = ''
    serializer_class = BoardSerializer

    
    def board_list(self, request, **kwargs):
        boards = Board.objects.filter(owner=request.user)
        serializer = self.serializer_class(boards, many=True)
        return Response(serializer.data, status=200)
        

    def board_create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            #import pdb; pdb.set_trace()
            serializer = serializer.save(owner=request.user)
            #import pdb; pdb.set_trace()
            return Response(serializer.title, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

    def board_detail(self, request, **kwargs):
        board = get_object_or_404(Board, id=kwargs.get('board_id'))
        serializer = self.serializer_class(board)
        return Response(serializer.data, status=200)

    def board_archive(self, request, **kwargs):
        board = get_object_or_404(Board, id=kwargs.get('board_id'))
        board.archive = True
        board.save()

        serializer = self.serializer_class(board)
        return Response(serializer.data, status=200)


class TrelloListViewSet(viewsets.ViewSet):

    queryset = ''
    serializer_class = TrelloListSerializer

    def trello_list(self, request, **kwargs):
        blists = TrelloList.objects.all()
        serializer = self.serializer_class(blists, many=True)
        return Response(serializer.data, status=200)

    def trello_list_create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer = serializer.save()
            return Response(serializer.title, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

    def trello_list_detail(self, request, **kwargs):
        blists = get_object_or_404(TrelloList, id=kwargs.get('list_id'), board_id=kwargs.get('board_id'))
        serializer = self.serializer_class(blists)
        return Response(serializer.data, status=200)

    def trello_list_archive(self, request, **kwargs):
        blists = get_object_or_404(TrelloList, id=kwargs.get('list_id'), baord_id=kwargs.get('board_id'))
        blists.archive = True
        blists.save()

        serializer = self.serializer_class(blists)
        return Response(serializer.data, status=200)

class CardViewSet(viewsets.ViewSet):

    queryset = ''
    serializer_class = CardSerializer

    def card_list(self, request, **kwargs):
        cards = Card.objects.all()
        serializer = self.serializer_class(cards, many=True)
        return Response(serializer.data,)

    def card_create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer = serializer.save()
            return Response(serializer.title, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

    def card_detail(self, request, **kwargs):
        cards = get_object_or_404(Card, id=kwargs.get('card_id'), trello_list_id=kwargs.get('list_id'))
        serializer = self.serializer_class(cards)
        return Response(serializer.data, status=200)

    def card_archive(self, request, **kwargs):
        cards = get_object_or_404(Card, id=kwargs.get('card_id'), trello_list_id=kwargs.get('list_id'))
        cards.archive = True
        cards.save()

        serializer = self.serializer_class(cards)
        return Response(serializer.data, status=200)


class UserViewSet(viewsets.ViewSet):

    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]
    #authentication_classes = [AllowAny,]
     

    def user_view(self, request, **kwargs):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        
        return Response(serializer.data)

     
    def user_login(self, request, **kwargs):
        import pdb; pdb.set_trace()

        username = request.data.get('username')
        password = request.data.get('password') 
        user = authenticate(request, username=username, password=password)
        user = User.objects.get(username=username)
        token = Token.objects.get(user=user)
        if user is not None:
            print('success')
            return Response(token.key, status=200)
        return Response(status=400)
            
    
    def user_create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer = serializer.save()
            return Response(serializer.username, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
    
    def user_detail(self, request, **kwargs):
        users = get_object_or_404(User, id=kwargs.get('user_id'))
        serializer = self.serializer_class(users)
        return Response(serializer.data, status=200)
    