from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name= models.CharField(max_length = 150, verbose_name= 'Nombre')
    created = models.DateTimeField(auto_now_add = True, verbose_name='Creacion')
    updated = models.DateTimeField(auto_now= True , verbose_name = 'Actualizacion')
    
    def __str__(self):
        text = '{0}'
        return text.format(self.name)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']
    
    
class Post(models.Model):
    title = models.CharField(max_length = 200, verbose_name= 'Titulo')
    content = models.TextField(verbose_name='Contenido') 
    published = models.DateTimeField(verbose_name='Fecha de publicacion', default = True)
    image = models.ImageField(verbose_name='Imagen',upload_to='blog', null=True , blank= True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete= models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name="get_posts")
    created = models.DateTimeField(auto_now_add = True, verbose_name='Creacion')
    updated = models.DateTimeField(auto_now= True , verbose_name = 'Actualizacion')
    
    def __str__(self) -> str:
        text = '{0}'
        return text.format(self.title)
    
    class Meta:
        verbose_name = 'Exponer'
        verbose_name_plural = 'Exponer'
        