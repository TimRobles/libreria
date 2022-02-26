from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'editorial_app'

urlpatterns = [
    path('prueba/', Prueba),
    path('primera-pagina/', Pagina1.as_view(), name='primera-pagina'),
    path('segunda-pagina/', Pagina2.as_view(), name='segunda-pagina'),
    path('lista/', EditorialListView.as_view(), name='lista'),
    path('add/', EditorialCreateView.as_view(), name='agregar'),
    path('update/<pk>/', EditorialUpdateView.as_view(), name='actualizar'),
    path('detalle/<pk>/', EditorialDetailView.as_view(), name='detalle'),
    path('eliminar/<pk>/', EditorialDeleteView.as_view(), name='eliminar'),
]