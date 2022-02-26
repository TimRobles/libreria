from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)

from .forms import *
from .models import *

# Create your views here.
def Prueba(request):
    return HttpResponse('Hola Mundo')

class Pagina1(TemplateView):
    template_name = "pagina1.html"

class Pagina2(TemplateView):
    template_name = "pagina2.html"


class EditorialListView(ListView):
    model = Editorial
    template_name = "editorial/list.html"
    context_object_name = 'contexto_editorial'

class EditorialCreateView(CreateView):
    model = Editorial
    template_name = "editorial/add.html"
    form_class = EditorialForm
    success_url = reverse_lazy('editorial_app:lista')

class EditorialUpdateView(UpdateView):
    model = Editorial
    template_name = "editorial/update.html"
    form_class = EditorialForm
    success_url = reverse_lazy('editorial_app:lista')

    
class EditorialDetailView(DetailView):
    model = Editorial
    template_name = "editorial/detail.html"
    context_object_name = 'contexto_editorial'


class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = "editorial/delete.html"
    context_object_name = 'contexto_editorial'
    success_url = reverse_lazy('editorial_app:lista')    
