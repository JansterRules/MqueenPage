from django.db import models

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    def __str__(self):
        return self.placa


class Mecanico(models.Model):
    rut = models.CharField(max_length=12, primary_key=True )
    dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField() # Email field para verificar "@"
    contraseña = models.CharField(max_length=100) 
    def __str__(self):
        return self.rut
    
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntergerField()
    def __str__(self):
        return f'{self.nombre} --> {self.precio}'

'''
NO OLVIDAR!!!!:


python manage.py makemigrations
python manage.py migrate



'''