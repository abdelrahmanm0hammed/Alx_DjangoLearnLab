from django.urls import path
from . import views
from .views import(
    PostDeleteView,
    PostCreateView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

urlpatterns = [

    path('',views.home,name='home'),
    path('register/', views.register,name='register'),
    path('post/',views.posts,name='posts'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('posts/',PostListView.as_view(), name='post-list'),
    path('posts/create/',PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDeleteView.as_view(), name='post-detail' ),
    path('posts/update/<int:pk>/', PostUpdateView.as_view, name='post-update'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view, name ='post-delete'),
 

]