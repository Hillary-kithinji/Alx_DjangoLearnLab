# api/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework import permissions


class BookList(generics.ListAPIView):
    """
    API view to list all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# New: BookViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD actions for the Book model
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # adjust as needed