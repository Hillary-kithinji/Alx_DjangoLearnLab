
---

#### `retrieve.md`

```markdown
# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
books
# <QuerySet [<Book: Book object (1)>]>
