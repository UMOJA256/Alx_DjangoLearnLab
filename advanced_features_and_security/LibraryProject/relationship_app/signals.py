from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings  # ✅ import settings
from .models import UserProfile

# Create UserProfile when a new user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
