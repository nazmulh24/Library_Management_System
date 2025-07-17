from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from catalog.views import AuthorViewSet, CategoryViewSet, BookViewSet


router = routers.DefaultRouter()  # ----> Api Root a error day na...link day...
router.register("authors", AuthorViewSet, basename="authors")
router.register("categories", CategoryViewSet, basename="categories")
router.register("books", BookViewSet, basename="books")


urlpatterns = [
    path("", include(router.urls)),
    # path
]
