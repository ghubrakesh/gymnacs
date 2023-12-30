from rest_framework import permissions

class IsTrainerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is a trainer or client (read only)
        return request.user and request.user.is_authenticated and request.method in permissions.SAFE_METHODS
