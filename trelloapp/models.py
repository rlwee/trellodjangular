from django.db import models
from django.conf import settings
from django.utils import timezone

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from PIL import Image
from rest_framework.authtoken.models import Token

from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
# Create your models here.



class Board(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class TrelloList(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)
    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=50)
    labels = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)
    trello_list = models.ForeignKey('TrelloList', on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    #import pdb; pdb.set_trace()
    if user_logged_in:
        token = Token.objects.get_or_create(user=instance)
        print(token)
