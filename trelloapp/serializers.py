from rest_framework import serializers
from .models import Board, TrelloList, Card
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password')

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.CharField(read_only=True, source='owner.username')

    class Meta:
        model = Board
        fields = ('id',
                  'title',
                  'date_created',
                  'owner',
                  'archive')


class TrelloListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrelloList
        fields = ('id',
                  'title',
                  'board',
                  'archive',
                  'date_created')

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('id',
                  'title',
                  'labels',
                  'date_created',
                  'trello_list',
                  'archive')