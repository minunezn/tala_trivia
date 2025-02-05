from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserCreateSerializer, TokenSerializer

class UserCreateView(generics.CreateAPIView):
    """ class CreateAPIView"""
    queryset = get_user_model().objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    """ Class TokenObtainPairView"""
    serializer_class = TokenSerializer

class TokenRefreshView(TokenRefreshView):
    pass
