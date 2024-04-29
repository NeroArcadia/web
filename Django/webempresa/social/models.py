from django.db import models

class link(models.Model):
    key =models.SlugField(verbose_name='nombre clabe', max_length=100 , unique= True)
    name = models.CharField(verbose_name='Red social', max_length= 100)
    url = models.URLField(verbose_name='Enlace', max_length= 120, null=True ,blank= True)
    created = models.DateTimeField(verbose_name='Creacion' , auto_now_add = True)
    updated = models.DateTimeField(verbose_name='Actualizacion', auto_now = True)
    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name']
        
    def __str__(self) :
        return self.name