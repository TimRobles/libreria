from django import forms

from .models import *

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'
    

