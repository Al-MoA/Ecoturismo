from django.db import models
  # Create your models here.

class Regiones(models.Model): #creacion de la tabla region
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self): #valor principal que muestra en la tabla region
        return self.nombre

class Comunas(models.Model):
    id_region = models.ForeignKey(Regiones, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Turista(models.Model):#creacion de tabla turista
    Run = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=10)
    Email = models.EmailField()

    def __str__(self):
        return self.Run
    

opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

class Carrucel(models.Model):
    imagen = models.ImageField(upload_to="imagenes") 