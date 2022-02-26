from django.db import models

from dateutil.relativedelta import relativedelta
from datetime import date

# Create your models here.

class Autor(models.Model):
    PAIS_CHOICES = (
        (1, 'Perú'),
        (2, 'Argentina'),
        (3, 'Colombia'),
        (4, 'Rusia'),
        (5, 'Ucrania'),
    )

    PROFESION_CHOICES = (
        ('Doc', 'Doctor'),
        ('Ing', 'Ingeniero'),
        ('Per', 'Periodista'),
        ('Esc', 'Escritor'),
    )

    Nombre = models.CharField(
        'Nombre',
        max_length=50,
        )
    Apellido = models.CharField(
        'Apellido',
        max_length=50,
        )
    Nacimiento = models.DateField(
        auto_now=False,
        auto_now_add=False,
        )
    Pais = models.IntegerField(
        'País',
        choices=PAIS_CHOICES,
        )
    Profesion = models.CharField(
        'Profesión',
        max_length=3,
        choices=PROFESION_CHOICES,
        )
    Foto = models.ImageField(
        'Foto',
        upload_to='img/Autor/',
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
        )
    Curriculum = models.FileField(
        'Curriculum',
        upload_to='file/Autor/',
        max_length=100,
        blank=True,
        null=True,
        )
    
    fecha_creacion = models.DateTimeField(
        'Fecha de creación',
        auto_now=False,
        auto_now_add=True,
        )
    fecha_actualizacion = models.DateTimeField(
        'Fecha de actualización',
        auto_now=True,
        auto_now_add=False,
        )

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['Profesion', 'Nombre']

    def full_name(self):
        return self.Nombre + ' ' + self.Apellido

    def get_edad(self):
        return relativedelta(date.today(), self.Nacimiento).years

    def __str__(self):
        return str(self.id) + '-' + self.full_name() + ' ' + self.get_Pais_display() + ' ' + self.get_Profesion_display()
