from django.db import models

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return self.placa


class Mecanico(models.Model):
    rut = models.CharField(max_length=8, primary_key=True)
    dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    contraseña = models.CharField(max_length=60)

'''
NO OLVIDAR!!!!:


python manage.py makemigrations
python manage.py migrate



'''