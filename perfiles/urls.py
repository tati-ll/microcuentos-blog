from django.urls import path
from django.views.generic import TemplateView

from perfiles import views

app_name = 'perfiles'

urlpatterns = [
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path("perfil/<int:pk>/", views.UsuarioDetailView.as_view(), name='perfil'),
    path('editar/<int:pk>/', views.UserUpdateView.as_view(), name='editar_usuario'),
    path('eliminar/<int:pk>/', views.UserDeleteView.as_view(), name="borrar_usuario"),
    path('mis_publicaciones/', views.user_posts, name='mis_publicaciones'),
    path('registro/', views.UsuarioRegistro.as_view(), name='registro_usuario'),
    path('success/', TemplateView.as_view(template_name='perfiles/registro_exitoso.html'), name="success"),
]
