from django.forms import ModelForm
from .models import Book

class ExampleForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_year')
