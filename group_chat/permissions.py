from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission:
    - Owners can CRUD their own objects.
    - Admins can CRUD their own objects.
    - No one can modify other admin/leader/superuser objects.
    - Everyone can read (GET, HEAD, OPTIONS) safely.
    """

    def has_object_permission(self, request, view, obj):
        # Allow safe methods for everyone
        if request.method in SAFE_METHODS:
            return True

        # Identify the owner of the object
        owner = getattr(obj, 'author', None) or getattr(obj, 'user', None)

        if owner is None:
            # fallback, deny just in case
            return False

        # Allow owner (even if admin) to modify their own objects
        if owner == request.user:
            return True

        # Block editing/deleting other admin/leader/superuser objects
        if owner.is_superuser or owner.is_admin or getattr(owner, 'is_leader', False):
            return False

        # Normal users cannot touch others' objects
        return False
