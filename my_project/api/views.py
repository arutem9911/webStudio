from rest_framework.viewsets import ModelViewSet
from accounts.models import Profile, User
from web.models import Order
from api import serializers
from .serializers import ProfileSerializer, UserSerializer, OrderSerializer
from django.contrib.auth import get_user_model

# Create your views here.


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = 'id'
    lookup_url_kwarg = 'id'
    method_serializers = {
        'get': serializers.UserSerializer,
        'put': serializers.UserUpdateSerializer,
        'patch': serializers.UserUpdateSerializer
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
        'get': serializers.OrderSerializer,
        'post': serializers.OrderCreateSerializer,
        'put': serializers.OrderCreateSerializer,
        'patch': serializers.OrderCreateSerializer
    }

    def get_serializer_class(self):
        method = self.request.method.lower()
        if method in self.method_serializers:
            return self.method_serializers.get(method)
        return self.serializer_class

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

