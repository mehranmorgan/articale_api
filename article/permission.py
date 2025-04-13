from rest_framework import permissions
from .models import BlockList

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        blockuser=BlockList.objects.filter(name=request.user.username).exists()
        return not blockuser


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user