from rest_framework import generics, permissions, viewsets, status
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


# -----------------------------
# Registration View
# -----------------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
# GenericAPIView Follow System
# -----------------------------
class FollowUserView(generics.GenericAPIView):       #  generics.GenericAPIView
    queryset = User.objects.all()                    #  CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            target = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=400)

        request.user.following.add(target)
        return Response({"detail": f"Now following {target.username}"}, status=200)


class UnfollowUserView(generics.GenericAPIView):     #  generics.GenericAPIView
    queryset = User.objects.all()                    #  CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            target = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

        request.user.following.remove(target)
        return Response({"detail": f"Unfollowed {target.username}"}, status=200)


# -----------------------------
# UserViewSet — Read-only + Follow actions
# -----------------------------
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'username'

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def follow(self, request, username=None):
        target = self.get_object()
        user = request.user

        if user == target:
            return Response({'detail': 'You cannot follow yourself.'}, status=400)

        user.following.add(target)
        return Response({'detail': f'Now following {target.username}'}, status=200)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unfollow(self, request, username=None):
        target = self.get_object()
        request.user.following.remove(target)
        return Response({'detail': f'Unfollowed {target.username}'}, status=200)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
