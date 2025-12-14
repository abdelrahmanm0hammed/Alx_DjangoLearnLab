from django.urls import path
from .views import followUserView, UnfollowUserView

from .views import(
    LoginView,
    RegisterView,
    ProfileView
)

urlpatterns=[
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('follow/<int:user_id>/', followUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name ='unfollow-user'),
]