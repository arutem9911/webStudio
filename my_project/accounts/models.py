from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from datetime import datetime


class User(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(unique=True, null=False, blank=False, editable=False, default=77777777777)
    photo = models.ImageField(upload_to='user', blank=True, null=True, default='user/default-avatar.jpg')
    birth_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата рождения')


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=50, blank=True, null=True, default='')
    last_name = models.CharField(max_length=50, blank=True, null=True, default='')
    city = models.CharField(max_length=20, blank=True, null=True, default='')

    def __str__(self):
        return self.user
