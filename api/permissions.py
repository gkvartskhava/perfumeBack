from rest_framework import permissions
from .models import CustomUser


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

class IsAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role==CustomUser.ADMIN


class CanDeleteReport(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == CustomUser.MANAGER

class Customer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == CustomUser.CUSTOMER






