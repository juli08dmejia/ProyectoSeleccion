from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='Productos'),
    path('adicionarProductos', views.adicionarProductos, name='adicionarProductos'),
]
