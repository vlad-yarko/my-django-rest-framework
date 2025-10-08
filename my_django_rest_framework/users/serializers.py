from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
