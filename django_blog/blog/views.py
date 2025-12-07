from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from rest_framework import generics
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, ListView , DeleteView, DetailView
from .models import Post
from .forms import PostForm

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


class PostListView(ListView):
   pass


class PostDetailView(DetailView):
  pass

class PostCreateView(LoginRequiredMixin, CreateView):
    model =Post
    form_class =PostForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = Post
   form_class = PostForm

   def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form) 
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
   
   pass


class PostDeleteView(DeleteView):
   pass

