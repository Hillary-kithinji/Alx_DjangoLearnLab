# Create Operation
```python
from bookshelf.models import Book

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output
book
# <Book: Book object (1)>
