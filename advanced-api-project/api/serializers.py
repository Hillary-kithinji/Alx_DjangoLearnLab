from rest_framework import serializers
from .models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer serializes all fields of the Book model.

    Validation:
    - Ensures publication_year is not in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation to prevent setting a publication year
        greater than the current year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer serializes the Author model.

    Includes:
    - name field
    - Nested BookSerializer to dynamically include all books
      written by the author.

    The 'books' field comes from the related_name defined
    in the Book model.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
