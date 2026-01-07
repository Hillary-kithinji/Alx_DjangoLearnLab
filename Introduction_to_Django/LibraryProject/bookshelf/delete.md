

---



\### \*\*4️⃣ delete.md\*\*



```markdown

\# Delete the Book instance



```python

from bookshelf.models import Book



\# Retrieve the book

book = Book.objects.get(title="Nineteen Eighty-Four")



\# Delete the book

book.delete()



\# Verify deletion

Book.objects.all()



\# <QuerySet \[]>



