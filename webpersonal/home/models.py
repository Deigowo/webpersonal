from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 50, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='images', verbose_name='Imagen', null=True, blank=True)
    url = models.URLField(verbose_name='Enlace', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'proyecto'
        ordering = ['-id']