from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username', read_only=True)
    post_id = serializers.IntegerField(source='post.id', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'sender', 'sender_username', 'notif_type', 'post', 'post_id', 'text', 'created_at', 'read']
        read_only_fields = ['id', 'recipient', 'sender', 'created_at', 'sender_username', 'post_id']

