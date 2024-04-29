from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length= 200 , verbose_name= 'Titulo')
    subtitle = models.CharField(max_length = 200 , verbose_name= 'Sub titulo')
    content = models.TextField()
    image = models.ImageField(verbose_name='Imagen',upload_to= 'image')
    created = models.DateTimeField(auto_now_add = True, verbose_name='Creacion')
    updated = models.DateTimeField(auto_now= True , verbose_name = 'Actualizacion')
    
    def __str__(self):
        text = '{0}, {1}'
        return text.format(self.title, self.subtitle)