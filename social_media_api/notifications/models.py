from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

User = settings.AUTH_USER_MODEL  # Use custom user model if any

class Notification(models.Model):
    recipient = models.ForeignKey(
        User,
        related_name='notifications',
        on_delete=models.CASCADE
    )
    actor = models.ForeignKey(
        User,
        related_name='actor_notifications',
        on_delete=models.CASCADE
    )
    verb = models.CharField(max_length=255)  # Describes the action (e.g., "liked", "followed")
    
    # Generic relation to any model (target object)
    target_content_type = models.ForeignKey(ContentType, blank=True, null=True, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    
    timestamp = models.DateTimeField(auto_now_add=True)  # When the action occurred

    read = models.BooleanField(default=False)  # Optional: mark notifications as read

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target} -> {self.recipient}"
