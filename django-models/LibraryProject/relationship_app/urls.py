from django.urls import path
from . import views

urlpatterns = [
    path('book_list/',views.book_list,name='book_list'),
    path('LibraryDetail/',views.LibraryDetailView, name='LibrayDetail')
]