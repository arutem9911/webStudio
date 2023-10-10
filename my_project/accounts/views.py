from rest_framework import status
from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import CreateView
from accounts.serializers import RegisterSerializer, LoginSerializer
from accounts.renderers import UserJSONRenderer
from accounts.models import User
from accounts.forms import RegisterForm


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        print(RegisterSerializer(request.data))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm

    def form_invalid(self, form):
        print(form.initial)

    def form_valid(self, form):
        user = form.save()
        User.objects.create(user=user)
        login(self.request, user)
        return redirect('main')
