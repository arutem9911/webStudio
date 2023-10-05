from rest_framework import serializers
from accounts.models import User
from django.contrib.auth import get_user_model
from web.models import Order
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, PasswordField
from rest_framework_simplejwt.views import TokenObtainPairView


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'phone', 'photo', 'birth_date', 'last_name', 'first_name']
        read_only = ['id', 'phone']


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(required=False)
    photo = serializers.ImageField(required=False)
    birth_date = serializers.DateTimeField(required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    first_name = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'photo', 'birth_date', 'last_name', 'first_name']
        read_only = ['id']


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'phone', 'first_name', 'last_name']


class OrderSerializer(serializers.ModelSerializer):
    author = AutorSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['title', 'description']


class LoginUserSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)
