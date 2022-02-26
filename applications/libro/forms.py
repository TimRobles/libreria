from django import forms

from .models import *

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'Autor': forms.CheckboxSelectMultiple(),
        }
    

