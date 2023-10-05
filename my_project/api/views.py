from rest_framework.viewsets import ModelViewSet
from accounts.models import User
from web.models import Order
from api import serializers
from api.serializers import UserSerializer, OrderSerializer, LoginUserSerializer, UserUpdateSerializer, OrderCreateSerializer
from django.contrib.auth import authenticate
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'id'
    lookup_url_kwarg = 'id'
    method_serializers = {
        'get': UserSerializer,
        'put': UserUpdateSerializer,
        'patch': UserUpdateSerializer
    }

    def get_serializer_class(self):
        method = self.request.method.lower()
        if method in self.method_serializers:
            return self.method_serializers.get(method)
        return self.serializer_class


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    method_serializers = {
        'get': OrderSerializer,
        'post': OrderCreateSerializer,
        'put': OrderCreateSerializer,
        'patch': OrderCreateSerializer
    }

    def get_serializer_class(self):
        method = self.request.method.lower()
        if method in self.method_serializers:
            return self.method_serializers.get(method)
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user_id)

