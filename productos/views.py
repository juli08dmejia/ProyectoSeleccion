from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Producto
from .forms import FormularioProducto

def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/productos.html", {"productos":productos})

def adicionarProductos(request):
    formulario_producto = FormularioProducto()
    return render(request, 'productos/adicionarProductos.html', {'miFormulario':formulario_producto})