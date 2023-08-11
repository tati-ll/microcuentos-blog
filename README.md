# Proyecto final del curso de programación con Python-Coderhouse

Autor: Tati Llaña.
Comisión: 55350.

Este es un proyecto de página web tipo blog realizado en el contexto del curso de programación con Python, dictado por la academia Coderhouse. La temática del blog son los microrrelatos.

## Funcionalidades y vistas incluidas

- Página Home, donde podrás ver los últimos 3 posts publicados. 
- Página about, donde podrás encontrar información sobre este blog.
- Lista de posts: Aquí podrás ver todos los post publicados, ordenados desde el más reciente hasta el más antiguo. Sólo verás algo de la información de cada post. Para verlo completo puedes hacer click a "Leer más".
- Vista detallada de un post: Luego de hacer click a "Leer más" podrás ver todo el contenido de un post.
- Lista de posts por categoría: Puedes acceder a ver los posts en cada categoría desde el navbar, en "categorias".
- Buscar posts: Puedes buscar posts desde la vista "Home", se buscará dentro del titulo y categoría de los posts en la base de datos, y se mostrará la lista de posts que correspondan. Si no hay posts coincidentes, se mostrará "Aún no hay publicaciones".
- Funcionalidades para usuarios: Se podrá crear nuevos usuarios, hacer Login y Logout.
- Al estar logueado el usuario podrá: Ver y modificar sus datos; crear, ver, modificar y eliminar sus posts; eliminar su cuenta.
- Usuarios no logueados pueden ver y buscar posts.  

## Instalación

1. Clona este repositorio.
2. Crea un entorno virtual y actívalo.
3. Instala las dependencias del proyecto: `pip install -r requirements.txt`
4. Realiza las migraciones: `python manage.py migrate`
5. Crea un superusuario: `python manage.py createsuperuser`
6. Ejecuta el servidor de desarrollo: `python manage.py runserver`

## Uso

Accede a la página web en http://localhost:8000/. Puedes iniciar sesión con tu superusuario o crear una nueva cuenta.

## Tecnologías Utilizadas

- Django
- Python
- HTML

## Créditos

- Tema utilizado: [https://themewagon.com/themes/topiclisting/]

## Contacto

Para preguntas o comentarios, puedes contactarme a través de mi perfil de GitHub: [https://github.com/tati-ll]
