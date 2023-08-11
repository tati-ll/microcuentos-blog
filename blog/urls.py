from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("pages/", views.lista_articulos, name="pages"),
    path("pages/<int:pk>", views.PostDetailView.as_view(), name="detalle"),
    path("categoria/<slug:slug>", views.CategoryListView.as_view(), name="categoria"),
    path("buscar/", views.Buscar.as_view(), name="buscar"),
    path("nuevo_post/", views.CrearPost, name="crear_post"),
    path('post/<int:pk>/editar/', views.PostUpdateView.as_view(), name='editar_post'),
    path('post/<int:pk>/eliminar/', views.PostDeleteView.as_view(), name='eliminar_post'),
]
