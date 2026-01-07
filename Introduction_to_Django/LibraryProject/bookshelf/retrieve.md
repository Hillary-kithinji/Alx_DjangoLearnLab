

---



\### \*\*2️⃣ retrieve.md\*\*



```markdown

\# Retrieve the Book instance



```python

from bookshelf.models import Book



\# Get all books

books = Book.objects.all()

books\[0].title

books\[0].author

books\[0].publication\_year



\# '1984'

\# 'George Orwell'

\# 1949



