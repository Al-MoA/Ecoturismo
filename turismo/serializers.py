from .models import Regiones, Contacto
from rest_framework import serializers

class RegionesSerializer(serializers.ModelSerializer):

    def validate_nombre(self, value):
        existe = Regiones.objects.filter(nombre=value).exists()
        if existe:
            raise serializers.ValidationError("El nombre ya existe")
        return value
    class Meta:
        model = Regiones
        fields = '__all__'