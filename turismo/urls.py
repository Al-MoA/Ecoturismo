from django.urls import path, include
from . import views
from .views import RegionesViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('Regiones', RegionesViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('Registro/', views.Registro, name="Registro"),
    path('Lugar1/', views.Lugar1, name='Lugar1'),
    path('inicarsesion/', views.IniciarSesion, name='IniciarSesion'),
    path('Contacto/', views.Contacto, name='Contacto'),
    path('agregar-cont/', views.agregar_cont, name= 'agregar-cont'),
    path('listar-cont/', views.listar_cont, name= 'listar-cont'),
    path('modificar-cont/<id>/', views.modificar_cont, name= "modificar-cont"),
    path('eliminar-cont/<id>/', views.eliminar_cont, name="eliminar-cont"),
    path('api/', include(routers.urls)),
    path('error_facebook/', views.error_facebook, name='error_facebook'),
]