from django.contrib import admin
from .models import Vehiculo, Mecanico, Producto

# Registramos Vehiculo
admin.site.register(Vehiculo)

# Registramos Mecanico
admin.site.register(Mecanico)

# Registramos Producto
admin.site.register(Producto)

# Registramos Carrito
#admin.site.register(Carrito)
