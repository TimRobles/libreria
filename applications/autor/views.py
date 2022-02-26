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
class AutorListView(ListView):
    model = Autor
    template_name = "autor/list.html"
    context_object_name = 'contexto_autor'

class AutorCreateView(CreateView):
    model = Autor
    template_name = "autor/add.html"
    form_class = AutorForm
    success_url = reverse_lazy('autor_app:lista')

class AutorUpdateView(UpdateView):
    model = Autor
    template_name = "autor/update.html"
    form_class = AutorForm
    success_url = reverse_lazy('autor_app:lista')

    
class AutorDetailView(DetailView):
    model = Autor
    template_name = "autor/detail.html"
    context_object_name = 'contexto_autor'

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = "autor/delete.html"
    context_object_name = 'contexto_autor'
    success_url = reverse_lazy('autor_app:lista')    