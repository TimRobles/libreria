from django.contrib import admin

from applications.editorial.models import Editorial

# Register your models here.

class EditorialAdmin(admin.ModelAdmin):
    list_display = (
        'RazonSocial',
        'Ruc',
        'Direccion',
        )
    list_filter = ('RazonSocial',)
    search_fields = ('Ruc',)
    
admin.site.register(Editorial, EditorialAdmin)
