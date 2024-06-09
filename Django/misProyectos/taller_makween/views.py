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
    return render(request, 'taller/vehiculos_list.html', context)
