from django_filters import rest_framework as filters

from catalog.models import Book


class BookFilter(filters.FilterSet):

    class Meta:
        model = Book
        fields = {
            "category_id": ["exact"],
            "author_id": ["exact"],
            "publication_date": ["gte", "lte"],
        }
