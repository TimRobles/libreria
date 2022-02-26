from django import forms

from .models import *

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

        widgets = {
            'Nacimiento': forms.DateInput(
                attrs={
                    'type':'date',
                },
                format='%Y-%m-%d',
            ),
        }
    

