from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "ProyectoSeleccionApp/home.html")

def tienda(request):
    return render(request, "ProyectoSeleccionApp/tienda.html")

def blog(request):
    return render(request, "ProyectoSeleccionApp/blog.html")

def contacto(request):
    return render(request, "ProyectoSeleccionApp/contacto.html")

def productos(request):
    return render(request, "ProyectoSeleccionApp/productos.html")

