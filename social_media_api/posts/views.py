from rest_framework import viewsets, permissions, mixins, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('comments', 'likes').all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
        # create notification (if notifications app connected)
        return Response({'detail': 'Liked'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({'detail': 'Unliked'}, status=status.HTTP_200_OK)
        return Response({'detail': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Comment.objects.select_related('author', 'post').all()
        post_id = self.request.query_params.get('post')
        if post_id:
            queryset = queryset.filter(post__id=post_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
