# users/permissions.py
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        print("super user", request.user.is_superuser(), request.user)
        return request.user and request.user.is_superuser()

class IsPlayer(permissions.BasePermission):
    def has_permission(self, request, view):
        print("player", request.user.is_superuser(), request.user)
        return request.user and request.user.is_superuser() == False
