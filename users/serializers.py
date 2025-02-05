from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    """ UserSerializer """

    class Meta:
        """ UserSerializer Behavior"""
        model = get_user_model()
        fields = ['id', 'username', 'email']

class UserCreateSerializer(serializers.ModelSerializer):
    """ UserCreateSerializer """

    class Meta:
        """ UserCreateSerializer Behavior"""
        model = get_user_model()
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create Behavior"""
        user = get_user_model().objects.create_user(**validated_data)
        return user

class TokenSerializer(serializers.Serializer):
    """ TokenSerializer """
    refresh = serializers.CharField()
    access = serializers.CharField()
