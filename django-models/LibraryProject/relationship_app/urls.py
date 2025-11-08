from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('list_books/',views.list_books,name='list_books'),
    path('LibraryDetail/',views.LibraryDetail, name='LibrayDetail')
]