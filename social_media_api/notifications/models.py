from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class Notification(models.Model):
    NOTIF_TYPE_CHOICES = (
        ('like', 'Like'),
        ('follow', 'Follow'),
        ('comment', 'Comment'),
    )

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications', null=True, blank=True)
    notif_type = models.CharField(max_length=20, choices=NOTIF_TYPE_CHOICES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification to {self.recipient.username} - {self.notif_type}"

