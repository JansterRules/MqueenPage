from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Vehiculo, Mecanico, Producto
from .forms import RegisterForm



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


# tienda

def tienda_view(request):
    productos = Producto.objects.all()
    return render(request, 'taller_makween/tienda.html', {'productos':productos})

def agregar_producto (request, producto_id):
    carrito = carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('taller_makween/tienda.html')

def restar_producto(request, producto_id):
    carrito = carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect ('taller_makween/tienda.html')

def limpiar_carrito(request):
    carrito=carrito(request)
    carrito.limpiar()
    return redirect('taller_makween/tienda.html')
    
def monto_total(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["total"])
    return {"monto_total": total}

# fin tienda

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = False  # ENTRAR COMO USUARIO ESTÁNDAR... EVITAR ADMINISTRADOR.
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login.html')

def home_view(request):
    return render(request, 'index')

def menu_view(request):
    request.session['usuario'] = request.user.username
    context = {'usuario': request.session['usuario']}
    return render(request, 'menu.html', context)

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
