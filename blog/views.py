from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.db.models import Q


from blog.models import Post, Categoria

def home(request):
    posts = Post.objects.order_by('-fecha')[:3]
    categorias = Categoria.objects.all()
    return render(request, 'blog/home.html', {'posts':posts,'categorias':categorias})

def about(request):
    categorias = Categoria.objects.all()
    return render(request, 'blog/about.html', {'categorias':categorias})

def lista_articulos(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'blog/pages.html', {'posts':posts, 'categorias':categorias})

class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class CategoryListView(generic.ListView):
    model = Post
    template_name = "blog/resultados.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    
    def get_queryset(self):
        query = self.request.path.replace('/categoria/', '')
        print(query)
        post_list = Post.objects.filter(categoria__slug=query)
        return post_list

class Buscar(generic.ListView):
    model = Post
    template_name = "blog/resultados.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('keyword')
        post_list = Post.objects.filter(
            Q(titulo__icontains=query) | Q(categoria__slug__icontains=query)
        ).distinct()
        return post_list