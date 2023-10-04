from django.urls import path, include
from accounts import views
from rest_framework import routers
from .views import ProfileViewSet, UserViewSet, OrderViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('user', UserViewSet)
router.register('order', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login', obtain_auth_token),
]
