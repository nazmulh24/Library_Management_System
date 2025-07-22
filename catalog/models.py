from django.db import models
from catalog.validators import validate_file_size

from cloudinary.models import CloudinaryField


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    photo = CloudinaryField(
        "photo",
        blank=True,
        null=True,
        validators=[validate_file_size],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="books",
    )
    publication_date = models.DateField(blank=True, null=True)
    publisher = models.CharField(max_length=150, blank=True, null=True)
    cover_image = CloudinaryField(
        "cover_image",
        blank=True,
        null=True,
        validators=[validate_file_size],
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        related_name="books",
    )
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def availability_status(self):
        return "Available" if self.available_copies > 0 else "Unavailable"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
