from django.shortcuts import render

from .models import Vehiculo

def index(request):
    context={}
    return render(request, 'taller_makween/index.html')

def base(request):
    context={}
    return render(request, 'taller_makween/base.html')

def aboutus(request):
    context={}
    return render(request, 'taller_makween/aboutus.html')

def Checkout(request):
    context={}
    return render(request, 'taller_makween/Checkout.html')

def faq(request):
    context={}
    return render(request, 'taller_makween/faq.html')

def galeria(request):
    context={}
    return render(request, 'taller_makween/galeria.html')

def login(request):
    context={}
    return render(request, 'taller_makween/login.html')

def register(request):
    context={}
    return render(request, 'taller_makween/register.html',)

def regvacante(request):
    context={}
    return render(request, 'taller_makween/regvacante.html',)

def crud(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'taller_makween/vehiculos_list.html', context)

def vehiculosAdd(request):
    if request.method == 'POST':
        placa = request.POST['placa']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        Vehiculo.objects.create(placa=placa, marca=marca, modelo=modelo)
        return redirect('crud')
    return render(request, 'taller_makween/vehiculos_add.html')

def vehiculos_del(request, pk):
    vehiculo = Vehiculo.objects.get(placa=pk)
    vehiculo.delete()
    return redirect('crud')

def vehiculos_findEdit(request, pk):
    vehiculo = Vehiculo.objects.get(placa=pk)
    context = {'vehiculo': vehiculo}
    return render(request, 'taller_makween/vehiculos_edit.html', context)
def vehiculosUpdate(request):
    if request.method == 'POST':
        placa = request.POST['placa']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        vehiculo = Vehiculo.objects.get(placa=placa)
        vehiculo.marca = marca
        vehiculo.modelo = modelo
        vehiculo.save()
        return redirect('crud')
