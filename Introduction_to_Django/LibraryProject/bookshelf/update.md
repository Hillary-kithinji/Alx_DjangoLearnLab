

---



\### \*\*3️⃣ update.md\*\*



```markdown

\# Update the Book title



```python

from bookshelf.models import Book



\# Retrieve the book

book = Book.objects.get(title="1984")



\# Update title

book.title = "Nineteen Eighty-Four"

book.save()



\# Verify update

Book.objects.all()



\# <QuerySet \[<Book: Nineteen Eighty-Four>]>



