from django.shortcuts import render, redirect, get_object_or_404
from .models import Regiones, Turista, Carrucel
from .form import ContactoForm, RegionForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):#muestra pagina inicial
    carrucel = Carrucel.objects.all()
    data = {
        'carrucel': carrucel
    }
    return render(request, 'turismo/index.html', data)

def Registro(request):#muestra pagina inicial
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def Lugar1(request):#muestra pagina inicial
    return render(request, 'turismo/Lugar1.html', {})

def IniciarSesion(request):#muestra pagina inicial
    return render(request, 'turismo/IniciarSesion.html', {})

def Contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    return render(request, 'turismo/Contacto.html', data)
@permission_required('turismo.add_regiones')
def agregar_region(request):
    data = {
        'form': RegionForm()
    }
    if request.method == 'POST':
        formulario = RegionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "region agregada"
        else:
            data["form"] = formulario
    return render(request, 'turismo/region/agregar.html', data)
@permission_required('turismo.view_regiones')
def listar_region(request):
    regions = Regiones.objects.all()
    data = {
        'regions' : regions
    }
    return render(request, 'turismo/region/listar.html', data)
@permission_required('turismo.change_regiones')
def modificar_region(request, id):
    region = get_object_or_404(Regiones, id_region=id)

    data = {
        'form' : RegionForm(instance=region)
    }
    if request.method == 'POST':
        formulario = RegionForm(data=request.POST, instance=region)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar-region")
        data["form"] = formulario
    return render(request, 'turismo/region/modificar.html', data)
@permission_required('turismo.delete_regiones')
def eliminar_region(request, id):
    region = get_object_or_404(Regiones, id_region=id)
    region.delete()
    return redirect(to="listar-region")


