from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    subtitulo = models.TextField()
    cuerpo = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.ManyToManyField('Categoria')
    imagen = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    class Meta:
        ordering = ('-fecha',)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)
            unique_slug = base_slug
            num = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

class Categoria(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo 
    
    class Meta:
        verbose_name_plural = 'categorias'
    
    def get_absolute_url(self):
        return reverse("blog:categoria", kwargs={"pk": self.pk})