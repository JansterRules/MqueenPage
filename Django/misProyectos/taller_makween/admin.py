from django.contrib import admin
from .models import Vehiculo, Mecanico, Producto, Carrito, CarritoProducto

# Registramos Vehiculo
admin.site.register(Vehiculo)

# Registramos Mecanico
admin.site.register(Mecanico)

# Registramos Producto
admin.site.register(Producto)

# Registramos Carrito
admin.site.register(Carrito)

# Registramos CarritoProducto
admin.site.register(CarritoProducto)
