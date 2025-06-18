from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    def __init__(self, roles):
        self.allowed_roles = roles

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role in self.allowed_roles
