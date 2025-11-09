from django.urls import path
from . import views
from .views import list_books
#from .views import LibraryDetail
from .views import login, logout, register

urlpatterns = [
    path('list_books/',views.list_books,name='list_books'),
   #path('LibraryDetail/',views.LibraryDetail, name='LibrayDetail'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register')
]