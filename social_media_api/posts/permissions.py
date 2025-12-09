from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow authors to edit/delete an object.
    """
    def has_object_permission(self, request, view, obj):
        # read permissions okay
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions only to author
        return obj.author == request.user
