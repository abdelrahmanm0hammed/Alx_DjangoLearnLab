from .models import Book , Author, Librarian, Library



books = Book.objects.all.filter(Author="")

all_books = ["Library.objects.get(name=library_name)", "books.all()"]


