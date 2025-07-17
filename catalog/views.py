from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from catalog.paginations import DefaultPagination
from catalog.models import Author, Category, Book
from catalog.serializers import AuthorSerializer, CategorySerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    pagination_class = DefaultPagination
