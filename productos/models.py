from django.db import models
from django.forms import ModelForm

# Create your models here.
class Producto(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    valorDetal = models.IntegerField()
    imagen = models.ImageField()
    #created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre
"""
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
"""
