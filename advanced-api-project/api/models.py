from django.db import models


class Author(models.Model):
    """
    Author model represents a writer who can have multiple books.

    Fields:
    - name: Stores the full name of the author.

    Relationship:
    - One Author can be associated with many Book instances.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an author.

    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: ForeignKey linking the book to an Author.

    Relationship:
    - Each Book belongs to one Author.
    - The related_name 'books' allows access via author.books.all().
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title
