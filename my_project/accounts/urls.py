from django.urls import path
from accounts.views import RegistrationAPIView, LoginAPIView, RegisterView


app_name = 'accounts'
urlpatterns = [
    path('api/register/', RegistrationAPIView.as_view(), name='register_api'),
    path('api/login/', LoginAPIView.as_view(), name='login_api'),
    path('registration/', RegisterView.as_view(), name='registration'),
]
