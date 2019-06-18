from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('email', 'username', 'user_type', 'password', 'balance')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
