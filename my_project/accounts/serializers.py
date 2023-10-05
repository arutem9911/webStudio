from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'phone', 'birth_date', 'username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    email = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        phone = data.get('phone', None)
        password = data.get('password', None)
        if phone is None:
            raise serializers.ValidationError(
                'A phone is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=phone, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'phone': user.phone,
            'username': user.username,
            'token': user.token
        }
