from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

from catalog.validators import validate_file_size
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"  # ---> Use email instead of username
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Member(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="member_profile",
    )
    membership_date = models.DateField(auto_now_add=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = CloudinaryField(
        "profile_picture",
        blank=True,
        null=True,
        validators=[validate_file_size],
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.email})"
