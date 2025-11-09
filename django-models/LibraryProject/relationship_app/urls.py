from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


from . import views
from .views import list_books
#from .views import LibraryDetail


urlpatterns = [
    path('list_books/',views.list_books,name='list_books'),
   #path('LibraryDetail/',views.LibraryDetail, name='LibrayDetail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/',views.register,name='register')
]