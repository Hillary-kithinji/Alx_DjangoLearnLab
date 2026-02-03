from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all Book instances.

    Access:
    - Public (read-only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single Book instance by ID.

    Access:
    - Public (read-only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Creates a new Book instance.

    Access:
    - Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing Book instance.

    Expects 'id' in request data (JSON body).

    Access:
    - Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        book_id = self.request.data.get("id")
        return get_object_or_404(Book, id=book_id)


class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a Book instance.

    Expects 'id' in request data (JSON body).

    Access:
    - Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        book_id = self.request.data.get("id")
        return get_object_or_404(Book, id=book_id)
