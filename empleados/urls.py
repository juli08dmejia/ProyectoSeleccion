from django.urls import path
from . import views

urlpatterns = [
    path('', views.empleados, name='Empleados'),
    #path('adicionarProductos', views.adicionarProductos, name='adicionarProductos'),
]