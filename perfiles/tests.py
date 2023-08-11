from django.test import TestCase

from perfiles.models import Usuario

class UsuarioTest(TestCase):
    def test_crear_usuario(self):
        # Crear un nuevo usuario
        usuario = Usuario.objects.create_user(username='nuevo_usuario', password='password123')
        
        # Comprobar que el usuario fue creado correctamente
        self.assertEqual(usuario.username, 'nuevo_usuario')
        self.assertTrue(usuario.check_password('password123'))
    
    def test_editar_usuario(self):
        # Crear un usuario de prueba para editar
        usuario = Usuario.objects.create_user(username='usuario_a_editar', password='password123')
        
        # Editar los datos del usuario
        usuario.first_name = 'Nuevo Nombre'
        usuario.last_name = 'Nuevo Apellido'
        usuario.save()
        
        # Obtener el usuario actualizado desde la base de datos
        usuario_actualizado = Usuario.objects.get(username='usuario_a_editar')
        
        # Comprobar que los datos se actualizaron correctamente
        self.assertEqual(usuario_actualizado.first_name, 'Nuevo Nombre')
        self.assertEqual(usuario_actualizado.last_name, 'Nuevo Apellido')
    
    def test_eliminar_usuario(self):
        # Crear un usuario para eliminar
        usuario = Usuario.objects.create_user(username='usuario_a_eliminar', password='password123')
        
        # Eliminar el usuario
        usuario.delete()
        
        # Comprobar que el usuario fue eliminado correctamente
        with self.assertRaises(Usuario.DoesNotExist):
            Usuario.objects.get(username='usuario_a_eliminar')


