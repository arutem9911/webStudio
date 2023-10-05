from rest_framework import serializers
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

