from django.db import models
from django.contrib.auth.models import User

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
    precio = models.IntegerField()
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'


# Modelo de Carrito funcional
class Carrito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carritos')
    productos = models.ManyToManyField(Producto, through='CarritoProducto')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrito del usuario: {self.user.username}'

    def agregar(self, producto): # Ageregar producto implementado desde "Carrito.py"
        carrito_producto, created = CarritoProducto.objects.get_or_create(carrito=self, producto=producto)
        if not created:
            carrito_producto.cantidad += 1
            carrito_producto.total += producto.precio
        else:
            carrito_producto.total = producto.precio
        carrito_producto.save()

    def eliminar(self, producto):
        CarritoProducto.objects.filter(carrito=self, producto=producto).delete()

    def restar(self, producto):
        try:
            carrito_producto = CarritoProducto.objects.get(carrito=self, producto=producto)
            carrito_producto.cantidad -= 1
            carrito_producto.total -= producto.precio
            if carrito_producto.cantidad <= 0:
                carrito_producto.delete()
            else:
                carrito_producto.save()
        except CarritoProducto.DoesNotExist:
            pass

    def limpiar_carro(self):
        CarritoProducto.objects.filter(carrito=self).delete()

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    total = models.PositiveIntegerField()

    def __str__(self):
        return f'Producto: {self.producto.nombre} | Cantidad: {self.cantidad}'

    def save(self, *args, **kwargs):
        self.total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs) # Buscar defiunición
  
'''
NO OLVIDAR!!!!:


python manage.py makemigrations
python manage.py migrate



'''