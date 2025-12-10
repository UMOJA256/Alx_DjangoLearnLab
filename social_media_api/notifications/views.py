from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    Returns a list of notifications for the logged-in user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')


class MarkNotificationReadView(generics.UpdateAPIView):
    """
    Mark a notification as read.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def perform_update(self, serializer):
        serializer.save(read=True)
