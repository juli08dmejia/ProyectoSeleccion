from django.db import models
from django.forms import ModelForm

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.tipo

class Empleado(models.Model):
    identificador = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'

    def __str__(self):
        return self.nombre
