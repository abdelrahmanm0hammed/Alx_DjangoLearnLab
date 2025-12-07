from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse

from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, ListView , DeleteView, DetailView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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
    return redirect('post-list')

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
    auth.logout(request)
    return render(request, 'blog/logout.html')

def profile(request):
    return render(request,'blog/profile.html')


class PostListView(ListView):
    model = Post
    template_name='blog/post_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()

        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name ='blog/post_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        # get the existing context (post details)
        context = super().get_context_data(**kwargs)

        # add an empty CommentForm to the context
        context['comments'] = Comment.objects.filter(post=self.object)

        return context


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
   template_name ='blog/post_confirm_delete.html'
   context_object_name = 'post'
   success_url = '/posts/'

   def test_func(self):
       post = self.get_object()

       return self.request.user == post.author
   

class CommentCreateView(LoginRequiredMixin, CreateView):
    model= Comment
    form_class = CommentForm
    template_name ='blog/comment_form.html'
    
    def form_valid(self, form):
        post_id = self.kwargs['pk']
        form.instance.post = get_object_or_404(Post, pk= post_id)
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the post to the template so the cancel link works
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    def get_success_url(self):
        return reverse('post-detail',kwargs={'pk':self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    context_object_name = 'comment'
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk':self.object.post.pk})