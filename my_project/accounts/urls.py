from django.urls import path
from accounts.views import RegistrationAPIView


app_name = 'accounts'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view(), name='registration'),
]
