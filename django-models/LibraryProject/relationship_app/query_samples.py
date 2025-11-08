from .models import Book , Author, Librarian, Library



books = Book.objects.all.filter(Author="")


