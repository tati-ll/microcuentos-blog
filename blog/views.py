from django.shortcuts import render

from blog.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

def about(request):
    return render(request, 'blog/about.html')

def lista_articulos(request):
    posts = Post.objects.all()
    return render(request, 'blog/pages.html', {'posts':posts})

