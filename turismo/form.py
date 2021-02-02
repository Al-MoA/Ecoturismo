from django import forms
from .models import Contacto, Regiones
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class RegionForm(forms.ModelForm):

    class Meta:
        model = Regiones
        fields = '__all__'
    
class CustomUserCreationForm(UserCreationForm):
    pass