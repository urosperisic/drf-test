from rest_framework import permissions

class IsAdminOrReadOnlyForUser(permissions.BasePermission):
    """
    - Admin: full access
    - User: read-only (GET, HEAD, OPTIONS) for all notes
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.method in permissions.SAFE_METHODS
