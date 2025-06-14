from rest_framework import permissions
from .models import CustomUser

from .permissions import IsStaffEditorPermission


class IsAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role==CustomUser.ADMIN


class CanDeleteReport(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == CustomUser.MANAGER

class Customer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == CustomUser.CUSTOMER




class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

