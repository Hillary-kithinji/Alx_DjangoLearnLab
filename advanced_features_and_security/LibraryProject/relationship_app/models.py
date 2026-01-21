from django.conf import settings
from django.db import models

# =========================
# UserProfile model
# =========================
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.email} ({self.role})"

# =========================
# Author model
# =========================
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# =========================
# Library model
# =========================
class Library(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# =========================
# Book model with custom permissions
# =========================
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, related_name="books", on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
