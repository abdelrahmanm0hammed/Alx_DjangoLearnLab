from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework
def register(request):

    if request.method =='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

        return render(request, 'blog/register.html',{'form':form})
    
def home(request):
    return render(request,'blog/home.html')

def posts(request):
    return render(request,'blog/posts.html')

def login(request):
    return render(request, 'blog/login.html')

def logout(request):
    return render(request, 'blog/logout.html')

def profile(request):
    return render(request,'blog/profile.html')


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'content', 'published_date', 'author']
    search_fields = ['title', 'content', 'published_date', 'author']
    ordering_fields = ['title', 'content', 'published_date', 'author']


class PostDetailView(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class = PostSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes =[TokenAuthentication]


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes =[TokenAuthentication]

