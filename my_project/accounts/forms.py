from django import forms
from django.contrib.auth import password_validation, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3 w-50'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3 w-50'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'phone', 'birth_date', 'username', 'password1', 'password2', 'first_name', 'last_name']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3 w-50', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3 w-50', 'required': True}),
            'phone': forms.NumberInput(attrs={'class': 'form-control mb-3 w-50', 'required': True}),
            'birth_date': forms.SelectDateWidget(attrs={'class': 'form-control mb-3 w-50', 'required': True}, years=range(1940, 2023)),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-3 w-50', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-3 w-50', 'required': True}),
        }

