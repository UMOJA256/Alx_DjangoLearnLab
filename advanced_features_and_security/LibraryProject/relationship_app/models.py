from django.db import models
from django.conf import settings

# Profile model
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

# Relationship model
class Relationship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('bookshelf.Book', on_delete=models.CASCADE)
    borrowed_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} borrowed {self.book}"
