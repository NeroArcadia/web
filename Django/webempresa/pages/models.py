from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length= 200 , verbose_name= 'Titulo')
    content = RichTextField(verbose_name='Contenido')
    
    class Meta:
        verbose_name ='Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['title']
    
    
    def __str__(self):
        text = '{0}'
        return text.format(self.title)