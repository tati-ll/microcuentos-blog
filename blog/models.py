from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    subtitulo = models.TextField()
    cuerpo = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ('-fecha',)