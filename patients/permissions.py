from rest_framework.permissions import BasePermission

class Permission(BasePermission):
    """
    Allows access to only doctors and receptioist
    """
    def has_permission(self,request,view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.role in ['DOCTOR', 'RECEPTIONIST','ADMIN']
        )