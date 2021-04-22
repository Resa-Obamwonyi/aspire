from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

import uuid


# Create your models here.
class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, null=False, unique=True)
    email = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'


class FavCharacter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_id = models.CharField(max_length=255)
    character_name = models.CharField(max_length=255)
    character_gender = models.CharField(max_length=255)
    character_race = models.CharField(max_length=255)


class FavQuote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_id = models.CharField(max_length=255)
    character_name = models.CharField(max_length=255, default="N/A")
    quote_id = models.CharField(max_length=255)
    quote_dialog = models.CharField(max_length=255)

