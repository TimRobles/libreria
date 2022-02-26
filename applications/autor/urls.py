from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'autor_app'

urlpatterns = [
    path('lista/', AutorListView.as_view(), name='lista'),
    path('add/', AutorCreateView.as_view(), name='agregar'),
    path('update/<pk>/', AutorUpdateView.as_view(), name='actualizar'),
    path('detalle/<pk>/', AutorDetailView.as_view(), name='detalle'),
    path('eliminar/<pk>/', AutorDeleteView.as_view(), name='eliminar'),
]