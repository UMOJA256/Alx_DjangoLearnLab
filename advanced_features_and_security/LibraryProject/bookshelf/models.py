from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

# ----------------------------
# Custom User Manager
# ----------------------------
class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser."""
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError(_('The Username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, **extra_fields)


# ----------------------------
# Custom User Model
# ----------------------------
class CustomUser(AbstractUser):
    """Custom user model with extra fields."""
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['username']


# ----------------------------
# Book Model with Custom Permissions
# ----------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)

    class Meta:
        permissions = [
            ("can_view", "Can view a book"),
            ("can_create", "Can create a book"),
            ("can_edit", "Can edit a book"),
            ("can_delete", "Can delete a book"),
        ]

    def __str__(self):
        return self.title






