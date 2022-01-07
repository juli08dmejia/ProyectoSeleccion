from django import forms

class FormularioProducto(forms.Form):
    codigo = forms.CharField(label="Codigo", required=True)
    nombre = forms.CharField(label="Nombre", required=True)
    valorDetal = forms.CharField(label="valorDetal", required=True)
