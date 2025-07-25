# Generated by Django 5.2.4 on 2025-07-22 16:05

import catalog.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('biography', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='authors/photos/', validators=[catalog.validators.validate_file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('isbn', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, max_length=150, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='books/covers/', validators=[catalog.validators.validate_file_size])),
                ('total_copies', models.PositiveIntegerField(default=1)),
                ('available_copies', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='catalog.author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='catalog.category')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
