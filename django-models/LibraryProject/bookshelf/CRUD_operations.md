create.md
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book



Expected Output:

<Book: 1984 by George Orwell (1949)>




retrieve.md

from bookshelf.models import Book

# Retrieve and display all attributes
book = Book.objects.get(title="1984")
book.title
book.author
book.publication_year

Expected Output:

'1984'
'George Orwell'
1949


update.md

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book


Expected Output:

<Book: Nineteen Eighty-Four by George Orwell (1949)>


delete.md

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()


Expected Output:

(1, {'bookshelf.Book': 1})
<QuerySet []>



