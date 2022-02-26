from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'libro_app'

urlpatterns = [
    path('lista/', LibroListView.as_view(), name='lista'),
    path('add/', LibroCreateView.as_view(), name='agregar'),
    path('update/<pk>/', LibroUpdateView.as_view(), name='actualizar'),
    path('detalle/<pk>/', LibroDetailView.as_view(), name='detalle'),
    path('eliminar/<pk>/', LibroDeleteView.as_view(), name='eliminar'),
    path('prueba/', Prueba.as_view(), name='prueba'),
]