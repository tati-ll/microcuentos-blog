from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})
