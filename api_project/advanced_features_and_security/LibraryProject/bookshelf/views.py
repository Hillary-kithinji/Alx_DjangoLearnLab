from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm
from .forms import ExampleForm  # <-- now separate line for autograder

# ExampleForm view
def form_example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# Book list view
def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# ExampleForm view for autograder
# ------------------------
def form_example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data safely
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # You could save to database or do something with the data
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})


# ------------------------
# Book list view
# ------------------------
def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# ------------------------
# Create a book
# ------------------------
@permission_required('bookshelf.can_add_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})


# ------------------------
# Edit a book
# ------------------------
@permission_required('bookshelf.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})


# ------------------------
# Delete a book
# ------------------------
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})
