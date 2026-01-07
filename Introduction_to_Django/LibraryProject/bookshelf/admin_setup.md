\# Django Admin Configuration for Book Model



\## Steps Taken



1\. Imported `Book` from `bookshelf.models`.

2\. Created `BookAdmin` class inheriting from `admin.ModelAdmin`.

3\. Configured `list\_display` to show `title`, `author`, `publication\_year`.

4\. Added `search\_fields` for `title` and `author`.

5\. Added `list\_filter` for `publication\_year`.

6\. Registered the `Book` model with `BookAdmin` using `admin.site.register(Book, BookAdmin)`.



\## Outcome



\- Book entries can now be viewed, searched, filtered, and managed in the Django admin interface.



