from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    View,
)

from .forms import *
from .models import *

# Create your views here.
class LibroListView(ListView):
    model = Libro
    template_name = "libro/list.html"
    context_object_name = 'contexto_libro'

class LibroCreateView(CreateView):
    model = Libro
    template_name = "libro/add.html"
    form_class = LibroForm
    success_url = reverse_lazy('libro_app:lista')

class LibroUpdateView(UpdateView):
    model = Libro
    template_name = "libro/update.html"
    form_class = LibroForm
    success_url = reverse_lazy('libro_app:lista')

    
class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detail.html"
    context_object_name = 'contexto_libro'

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "libro/delete.html"
    context_object_name = 'contexto_libro'
    success_url = reverse_lazy('libro_app:lista')    

class Prueba(View):
    template_name = "prueba.html"
    context = {
        'respuesta_get' : None,
        'respuesta_get_segundo' : None,
    }

    def get(self, request, *args, **kwargs):
        self.context['respuesta_get'] = request.GET.get('Prueba-Get')
        self.context['respuesta_get_segundo'] = request.GET.get('Prueba-Get-segundo')
        return render(
            request = request,
            template_name = self.template_name,
            context = self.context
        )