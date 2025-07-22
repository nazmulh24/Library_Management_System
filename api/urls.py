from django.urls import path, include
from rest_framework_nested import routers

from catalog.views import AuthorViewSet, CategoryViewSet, BookViewSet
from circulation.views import BorrowRecordViewSet


router = routers.DefaultRouter()  # ----> Api Root a error day na...link day...
router.register("authors", AuthorViewSet, basename="authors")
router.register("categories", CategoryViewSet, basename="categories")
router.register("books", BookViewSet, basename="books")
router.register("borrow-records", BorrowRecordViewSet, basename="borrow-records")


urlpatterns = [
    path("", include(router.urls)),
]
