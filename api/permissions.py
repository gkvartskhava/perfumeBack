# from rest_framework import permissions
# from .models import CustomUser

# class IsAdministrator(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role==CustomUser.ADMINISTRATOR


# class CanDeleteReport(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user.role == CustomUser.COURIER

# class CanAddReport(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user.role == CustomUser.OFFICE_WORKER