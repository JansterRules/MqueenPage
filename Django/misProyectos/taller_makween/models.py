from django.db import models

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return self.placa

'''
NO OLVIDAR!!!!:


python manage.py makemigrations
python manage.py migrate



'''