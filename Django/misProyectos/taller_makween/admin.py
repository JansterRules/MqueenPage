from django.contrib import admin
from .models import Vehiculo, Mecanico

# Register your models here.
# Registramos Vehiculo
admin.site.register(Vehiculo)
# Registramos Mecnaico
admin.site.register(Mecanico)