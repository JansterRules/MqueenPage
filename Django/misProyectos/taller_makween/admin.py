from django.contrib import admin
from .models import Vehiculo, Mecanico, Producto

# Register your models here.
# Registramos Vehiculo
admin.site.register(Vehiculo)
# Registramos Mecnaico
admin.site.register(Mecanico)
# Registramos Productos
admin.site.register(Producto)