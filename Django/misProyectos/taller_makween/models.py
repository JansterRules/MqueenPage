from django.db import models

# Modelo de Vehículo (retiramos los anteriores s por mero hecho de no utilizarlos)
class Vehiculo(models.Model):
    placa  = models.CharField(max_length=10, primary_key=True)
    marca  = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año    = models.IntegerField()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"
