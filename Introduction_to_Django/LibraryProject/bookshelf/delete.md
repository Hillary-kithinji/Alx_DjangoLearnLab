
---

#### `delete.md`

```markdown
# Delete Operation

```python
from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>
