from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehiculo, Mecanico

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
        return redirect('crud')

    return render(request, 'taller_makween/vehiculos_add.html')

def vehiculos_del(request, pk):
    vehiculo = get_object_or_404(Vehiculo, placa=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('crud')
    context = {'vehiculo': vehiculo}
    return render(request, 'taller_makween/vehiculos_confirm_delete.html', context)

def vehiculos_findEdit(request, pk):
    vehiculo = get_object_or_404(Vehiculo, placa=pk)
    context = {'vehiculo': vehiculo}
    return render(request, 'taller_makween/vehiculos_edit.html', context)

def vehiculosUpdate(request):
    if request.method == 'POST':
        placa = request.POST['placa']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        año = request.POST['año']
        vehiculo = get_object_or_404(Vehiculo, placa=placa)
        vehiculo.marca = marca
        vehiculo.modelo = modelo
        vehiculo.año = año
        vehiculo.save()
        return redirect('crud')
    return render(request, 'taller_makween/vehiculos_edit.html')

def crud_mecanicos(request):
    mecanicos = Mecanico.objects.all()
    context = {'mecanicos': mecanicos}
    print("probando views.py crudmecanicos")
    return render(request, "taller_makween/mecanico_list.html", context)

def mecanico_add(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        dv = request.POST['dv']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        email = request.POST['email']
        contraseña = request.POST['contrasena']
        Mecanico.objects.create(rut=rut, dv=dv, nombres=nombres, apellidos=apellidos, email=email, contraseña=contraseña)
        return redirect('crud_Mecanicos')
    return render(request, 'taller_makween/mecanico_add.html')


def mecanico_del(request, pk):
    mecanico = get_object_or_404(Mecanico, rut=pk)
    if request.method == 'POST':
        mecanico.delete()
        return redirect('crud_Mecanicos')
    context = {'mecanico': mecanico}
    return render(request, 'taller_makween/mecanico_confirm_delete.html', context)

def mecanico_edit(request, pk):
    mecanico = get_object_or_404(Mecanico, rut=pk)
    if request.method == 'POST':
        mecanico.dv = request.POST['dv']
        mecanico.nombres = request.POST['nombres']
        mecanico.apellidos = request.POST['apellidos']
        mecanico.email = request.POST['email']
        mecanico.contraseña = request.POST['contraseña']
        mecanico.save()
        return redirect('crud_Mecanicos')
    context = {'mecanico': mecanico}
    return render(request, 'taller_makween/mecanico_edit.html', context)

def vehiculos_findEdit(request, pk): # Se desarrollo para evitar el error en la actualización de valores dentro del CRUD.
    # Es una combinación entre 'vehiculos_findEdit' y 'vehiculosUpdate'
    vehiculo = get_object_or_404(Vehiculo, placa=pk)
    if request.method == 'POST':
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        año = request.POST['año']
        vehiculo.marca = marca
        vehiculo.modelo = modelo
        vehiculo.año = año
        vehiculo.save()
        return redirect('crud')
    context = {'vehiculo': vehiculo}
    return render(request, 'taller_makween/vehiculos_edit.html', context)
