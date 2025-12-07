from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView

from rest_framework import generics
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, ListView , DeleteView, DetailView
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('login')
    else :
        return render(request, 'blog/login.html')

def logout(request):
    return render(request, 'blog/logout.html')

def profile(request):
    return render(request,'blog/profile.html')


class PostListView(ListView):
    model = Post
    template_name='blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name ='blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model =Post
    form_class =PostForm
    template_name='blog/post_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})
  


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = Post
   form_class = PostForm
   template_name='blog/post_form.html'

   def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form) 
   def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
   def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})
   
   


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Post
   form_class = PostForm
   template_name ='blog/post_confirm_delete.html'
   context_object_name = 'post'
   success_url = '/posts/'

   def test_func(self):
       post = self.get_object()

       return self.request.user == post.author
   

