from django.db import models

from applications.autor.models import Autor
from applications.editorial.models import Editorial

# Create your models here.

class Libro(models.Model):
    Titulo = models.CharField('Título', max_length=100)
    Year = models.IntegerField('Año')
    Paginas = models.IntegerField('Páginas')
    Portada = models.ImageField(upload_to='img/Libro', height_field=None, width_field=None, max_length=None)
    Editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    Autor = models.ManyToManyField(Autor)


    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.Titulo + ' ' + self.Editorial.Nombre

