from rest_framework import serializers

from catalog.models import Author, Category, Book


class AuthorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name="get_full_name")

    class Meta:
        model = Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "biography",
            "birth_date",
            "death_date",
            "photo",
        ]

    def get_full_name(self, obj):
        return str(obj)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField(method_name="get_author_name")
    category_name = serializers.SerializerMethodField(method_name="get_category_name")

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "subtitle",
            "isbn",
            "description",
            "cover_image",
            "category",
            "category_name",
            "publication_date",
            "publisher",
            "author",
            "author_name",
            "total_copies",
            "available_copies",
            "availability_status",
        ]

    def get_author_name(self, obj):
        return str(obj.author)

    def get_category_name(self, obj):
        return obj.category.name
