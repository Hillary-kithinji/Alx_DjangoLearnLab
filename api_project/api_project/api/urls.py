# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Single urlpatterns list
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # optional list view
    path('', include(router.urls)),                         # router URLs for CRUD
]
