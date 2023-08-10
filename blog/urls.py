from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("pages/", views.lista_articulos, name="pages"),
    path("pages/<int:pk>", views.PostDetailView.as_view(), name="detalle"),
    path("categoria/<slug:slug>", views.CategoryListView.as_view(), name="categoria"),
    path("buscar/", views.Buscar.as_view(), name="buscar"),
]
