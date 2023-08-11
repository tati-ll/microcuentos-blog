from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import Post

class PostTest(TestCase):
    """En esta clase están todas las pruebas del modelo Post"""

    def setUp(self):
        # Crear un usuario para usar en las pruebas
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        
        # Crear un objeto Post para usar en las pruebas
        self.post = Post.objects.create(
            titulo="Titulo",
            subtitulo="subtitulo",
            cuerpo="Texto, texto, texto",
            autor=self.user
        )

        # Comprobar que el post fue creado y la data se guardó correctamente
        self.assertIsNotNone(self.post)
        self.assertEqual(self.post.titulo, "Titulo")
        self.assertEqual(self.post.subtitulo, "subtitulo")
        self.assertEqual(self.post.cuerpo, "Texto, texto, texto")
        self.assertEqual(self.post.autor, self.user)

    def test_editar_post(self):
        # Editar el objeto Post
        self.post.titulo = "Nuevo Titulo"
        self.post.save()

        # Comprobar que los cambios se guardaron correctamente
        self.assertEqual(self.post.titulo, "Nuevo Titulo")

    def test_eliminar_post(self):
        # Eliminar el objeto Post
        self.post.delete()

        # Comprobar que el objeto se eliminó correctamente
        self.assertEqual(Post.objects.count(), 0)

