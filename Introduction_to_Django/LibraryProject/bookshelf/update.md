
---

#### `update.md`

```markdown
# Update Operation

```python
from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
book.title
# 'Nineteen Eighty-Four'
