from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import ObtainAuthToken
from trelloapp.views import (BoardViewSet,
                             TrelloListViewSet,
                            #  api_root,
                             CardViewSet,
                             UserViewSet
                                )


urlpatterns = [
    # path('',api_root),
    path('boards/', BoardViewSet.as_view({'get':'board_list','post':'board_create'}),name='boards'),
    path('lists/', TrelloListViewSet.as_view({'get':'trello_list','post':'trello_list_create'}), name='lists'),
    path('cards/', CardViewSet.as_view({'get':'card_list','post':'card_create'}),name='cards'),
    path('boards/<int:board_id>/', BoardViewSet.as_view({'get':'board_detail','post':'board_archive'})),
    path('board/<int:board_id>/list/<int:list_id>/', TrelloListViewSet.as_view({'get':'trello_list_detail','post':'trello_list_archive'}), name='list-detail'),
    path('board/<int:board_id>/list/<int:list_id>/card/<int:card_id>/', CardViewSet.as_view({'get':'card_detail','post':'card_archive'}), name='card-archive'),
    path('users/', UserViewSet.as_view({'get':'user_view', 'post':'user_login'}),name='users'),
    path('user/<int:user_id>/', UserViewSet.as_view({'get':'user_detail'}),name='users'),

    
]

urlpatterns = format_suffix_patterns(urlpatterns)