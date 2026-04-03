from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == 'admin'

class IsAnalyst(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role in ['admin', 'analyst']

class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return True
