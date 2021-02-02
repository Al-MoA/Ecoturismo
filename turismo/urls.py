from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Registro/', views.Registro, name="Registro"),
    path('Lugar1/', views.Lugar1, name='Lugar1'),
    path('inicarsesion/', views.IniciarSesion, name='IniciarSesion'),
    path('Contacto/', views.Contacto, name='Contacto'),
    path('agregar-region/', views.agregar_region, name= 'agregar-region'),
    path('listar-region/', views.listar_region, name= 'listar-region'),
    path('modificar-region/<id>/', views.modificar_region, name= "modificar-region"),
    path('eliminar-producto/<id>/', views.eliminar_region, name="eliminar-region"),
    
]