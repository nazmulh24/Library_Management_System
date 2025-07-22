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

from drf_yasg.utils import swagger_auto_schema


class AuthorViewSet(ModelViewSet):
    """
    Manage authors in the library system with CRUD operations
    - Full access for librarians, read-only for users
    - Standard CRUD operations: Create, Read, Update, Delete
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    permission_classes = [IsLibrarianOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve a list of authors")
    def list(self, request, *args, **kwargs):
        """Retrieve all the Authors"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create an author by admin",
        operation_description="This allow an admin to create an author",
        request_body=AuthorSerializer,
        responses={201: AuthorSerializer, 400: "Bad Request"},
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create Authors"""
        return super().create(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):
    """
    Manage categories in the library system with CRUD operations
    - Full access for librarians, read-only for users
    - Standard CRUD operations: Create, Read, Update, Delete
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsLibrarianOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve a list of categories")
    def list(self, request, *args, **kwargs):
        """Retrieve all the Categories"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a category by admin",
        operation_description="This allow an admin to create a category",
        request_body=CategorySerializer,
        responses={201: CategorySerializer, 400: "Bad Request"},
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create Categories"""
        return super().create(request, *args, **kwargs)


class BookViewSet(ModelViewSet):
    """
    Manage books in the library system with CRUD operations
     - Search: title, subtitle, isbn
     - Filter: category, author, publication_year, available_copies
     - Order: created_at, updated_at, title
     - Custom endpoints: popular/ (top 10 borrowed), available/ (in stock)
    """

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

    @swagger_auto_schema(operation_summary="Retrieve a list of books")
    def list(self, request, *args, **kwargs):
        """Retrieve all the Books"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a book by admin",
        operation_description="This allow an admin to create a book",
        request_body=BookSerializer,
        responses={201: BookSerializer, 400: "Bad Request"},
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create Books"""
        return super().create(request, *args, **kwargs)
