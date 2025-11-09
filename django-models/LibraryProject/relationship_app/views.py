from django.shortcuts import render, redirect
from .models import Book
from .models import Author
from .models import Library
from .models import Librarian
from django.views.generic.detail import DetailView
from django.db import models
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def login(request):
    return render(request, 'relationship_app/login.html')

def logout(request):
    return render(request, 'relationship_app/logout.html')

def register(request):
    return render(request, 'relationship_app/register.html')

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

def register(request):
    if request.method == "POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        
        return render(request, 'relationship_app/register.html',{'form':form})
    