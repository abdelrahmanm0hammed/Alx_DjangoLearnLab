from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('register/', views.register,name='register'),
    path('post/',views.posts,name='posts'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
 

]