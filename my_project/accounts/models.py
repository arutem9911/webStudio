from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.utils import timezone
import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone, birth_date, email, password=None):
        if username is None:
            raise TypeError('Users must have a username')
        if phone is None:
            raise TypeError('Users must have a phone')
        user = self.model(username=username, phone=phone, birth_date=birth_date, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, phone, password, birth_date, email):
        if password is None:
            raise TypeError('Superuser must have a password')
        user = self.create_user(username, phone, password, birth_date, email)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(db_index=True, unique=True, null=False, blank=False)
    photo = models.ImageField(upload_to='user', blank=False, null=False, default='user/default-avatar.jpg')
    birth_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата рождения')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=30, null=True, default=None)
    last_name = models.CharField(max_length=20, null=True, default=None)
    date_joined = models.DateField(default=timezone.now)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'birth_date', 'email']
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token
