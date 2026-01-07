from django.contrib import admin
from .models import Book

# Customize the admin interface for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    search_fields = ('title', 'author')                     # Enable search
    list_filter = ('publication_year',)                     # Filter by publication year

# Register the Book model with the admin
admin.site.register(Book, BookAdmin)
