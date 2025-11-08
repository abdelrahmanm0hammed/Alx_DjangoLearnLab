from django.shortcuts import render
from .models import Book, Author, Library, Librarian
from django.views.generic import DetailView

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'