from django.shortcuts import render, redirect, get_object_or_404
from .models import Regiones, Turista, Carrucel, Contacto
from .form import ContactoForm, RegionForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import RegionesSerializer
from urllib.request import urlopen
import json

class RegionesViewSet(viewsets.ModelViewSet):
    queryset = Regiones.objects.all()
    serializer_class = RegionesSerializer

# Create your views here.
def index(request):#muestra pagina inicial
    carrucel = Carrucel.objects.all()
    
    url = "https://api.gael.cl/general/public/clima/SCQN"
    datos = urlopen(url).read()
    Temp = json.loads(datos)
    clima = Temp["Temp"]
    
    return render(request, 'turismo/index.html',{'carrucel': carrucel,'clima':clima})

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


def agregar_cont(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario
    return render(request, 'turismo/contacto/agregar.html', data)

def listar_cont(request):
    contact = Contacto.objects.all()
    data = {
        'contact' : contact
    }
    return render(request, 'turismo/contacto/listar.html', data)

def modificar_cont(request, id):
    con = get_object_or_404(Contacto, id=id)

    data = {
        'form' : ContactoForm(instance=con)
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST, instance=con)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar-cont")
        data["form"] = formulario
    return render(request, 'turismo/contacto/modificar.html', data)

def eliminar_cont(request, id):
    cont = get_object_or_404(Contacto, id=id)
    cont.delete()
    return redirect(to="listar-cont")

def error_facebook(request):
    return render(request, 'registration/error_facebook.html')

