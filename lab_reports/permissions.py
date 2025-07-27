from rest_framework.permissions import BasePermission

class LabReportPermission(BasePermission):
    """
    Allows access to lab reports for lab staff and admin users only
    """
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.role in ['LAB', 'ADMIN']
        ) 