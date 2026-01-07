\# Create a Book instance



```python

from bookshelf.models import Book



\# Create a book

book = Book(title="1984", author="George Orwell", publication\_year=1949)

book.save()



\# Check saved book

Book.objects.all()



\# <QuerySet \[<Book: 1984>]>



