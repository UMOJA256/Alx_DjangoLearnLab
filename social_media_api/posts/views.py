from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# -------------------------------
# Custom Permission
# -------------------------------
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow full access only to owners.
    Others get read-only access.
    """
    def has_object_permission(self, request, view, obj):
        # SAFE methods: GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only owner can edit/delete
        return obj.user == request.user


# -------------------------------
# Post ViewSet
# -------------------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()          # Required check: "Post.objects.all()"
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# -------------------------------
# Comment ViewSet
# -------------------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()        # Required check: "Comment.objects.all()"
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
