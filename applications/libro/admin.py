from django.contrib import admin

from .models import *
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display = (
        'Titulo',
        'Year',
        'Paginas',
        )
    
admin.site.register(Libro, LibroAdmin)