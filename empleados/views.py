from django.shortcuts import render
from .models import Empleado, Categoria

# Create your views here.
def empleados(request):
    empleados = Empleado.objects.all()
    return render(request, "empleados/empleados.html", {"empleados":empleados})

def categoria(request, categoria_tipo):
    categoria = Categoria.objects.get(tipo=categoria_tipo )
    empleado = Categoria.objects.filter(categorias=categoria)
    return render(request,"blog/categoria.html", {'categoria':categoria, 'empleado':empleados})

