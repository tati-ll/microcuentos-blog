from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from blog.models import Post, Categoria
from blog.forms import PostForm

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
    
@login_required
def CrearPost(request):
    if request.method == 'POST':
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('perfiles:mis_publicaciones') 
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'cuerpo', 'categoria']
    template_name = 'blog/post_form.html'
    success_url= reverse_lazy('perfiles:mis_publicaciones')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(autor=self.request.user)
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('perfiles:mis_publicaciones')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(autor=self.request.user)
