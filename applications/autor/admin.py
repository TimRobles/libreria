from django.contrib import admin

from .models import Autor
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'Nombre',
        'Apellido',
        'Pais',
        'Profesion',
        )
    
admin.site.register(Autor, AutorAdmin)