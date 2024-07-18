
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Author, Book, BorrowRecord
from .forms import AuthorForm, BookForm, BorrowRecordForm


# Views for adding records

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  # Redirect to author list view
    else:
        form = AuthorForm()
    return render(request, 'app/add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list view
    else:
        form = BookForm()
    return render(request, 'app/add_book.html', {'form': form})

def add_borrow_record(request):
    if request.method == 'POST':
        form = BorrowRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrow_record_list')  # Redirect to borrow record list view
    else:
        form = BorrowRecordForm()
    return render(request, 'app/add_borrow_record.html', {'form': form})

# Views for displaying paginated lists

class AuthorListView(ListView):
    model = Author
    template_name = 'app/author_list.html'
    paginate_by = 10

class BookListView(ListView):
    model = Book
    template_name = 'app/book_list.html'
    paginate_by = 10

class BorrowRecordListView(ListView):
    model = BorrowRecord
    template_name = 'app/borrow_record_list.html'
    paginate_by = 10







