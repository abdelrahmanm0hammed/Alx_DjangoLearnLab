from .models import Book , Author, Librarian, Library



books = Book.objects.filter(author=Author.objects.get(name=author_name))
all_books = ["Library.objects.get(name=library_name)", "books.all()"]
librarian = ["Librarian.objects.get(library="]

