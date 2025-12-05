from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

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