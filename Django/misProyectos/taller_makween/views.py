from django.shortcuts import render
from .models import Vehiculo

def index(request):
    context = {}
    return render(request, 'taller_makween/index.html', context)

def base(request):
    context = {}
    return render(request, 'taller_makween/base.html', context)

def aboutus(request):
    context = {}
    return render(request, 'taller_makween/aboutus.html', context)

def Checkout(request):
    context = {}
    return render(request, 'taller_makween/Checkout.html', context)

def faq(request):
    context = {}
    return render(request, 'taller_makween/faq.html', context)

def galeria(request):
    context = {}
    return render(request, 'taller_makween/galeria.html', context)

def login(request):
    context = {}
    return render(request, 'taller_makween/login.html', context)

def register(request):
    context = {}
    return render(request, 'taller_makween/register.html', context)

def regvacante(request):
    context = {}
    return render(request, 'taller_makween/regvacante.html', context)

def crud(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'taller_makween/vehiculos_list.html', context)

def vehiculosAdd(request):
    if request.method == 'POST':
        placa = request.POST['placa']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        año = request.POST['año']
        Vehiculo.objects.create(placa=placa, marca=marca, modelo=modelo, año=año)
        return crud(request) # Activar renderizardo
    return render(request, 'taller_makween/vehiculos_add.html')

def vehiculos_del(request, pk):
    vehiculo = Vehiculo.objects.get(placa=pk)
    vehiculo.delete()
    return crud(request)  # Activar renderizardo

def vehiculos_findEdit(request, pk):
    vehiculo = Vehiculo.objects.get(placa=pk)
    context = {'vehiculo': vehiculo}
    return render(request, 'taller_makween/vehiculos_edit.html', context)

def vehiculosUpdate(request):
    if request.method == 'POST':
        placa = request.POST['placa']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        año = request.POST['año']
        vehiculo = Vehiculo.objects.get(placa=placa)
        vehiculo.marca = marca
        vehiculo.modelo = modelo
        vehiculo.año = año
        vehiculo.save()
        return crud(request)  # Renderizar la vista crud
    return render(request, 'taller_makween/vehiculos_edit.html')
