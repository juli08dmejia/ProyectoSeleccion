from django.contrib import admin
from .models import Producto

# Register your models here.

admin.site.register(Producto)
#Register your models here.
#class ProductoAdmin(admin.ModelAdmin):
#    readonly_fields=('created','updated')

#admin.site.register(Servicio, ServicioAdmin)

