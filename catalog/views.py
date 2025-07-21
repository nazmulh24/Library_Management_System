from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count, Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from catalog.filters import BookFilter
from catalog.paginations import DefaultPagination
from catalog.models import Author, Category, Book
from catalog.serializers import (
    AuthorSerializer,
    CategorySerializer,
    BookSerializer,
)

from circulation.permissions import IsLibrarianOrReadOnly


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    permission_classes = [IsLibrarianOrReadOnly]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsLibrarianOrReadOnly]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsLibrarianOrReadOnly]
    pagination_class = DefaultPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ["title", "subtitle", "isbn"]
    ordering_fields = ["created_at", "updated_at", "title"]

    @action(detail=False, methods=["get"])
    def popular(self, request):
        books = Book.objects.annotate(borrow_count=Count("borrow_records")).order_by(
            "-borrow_count"
        )[:10]
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def available(self, request):
        books = Book.objects.filter(available_copies__gt=0).order_by("id")
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

