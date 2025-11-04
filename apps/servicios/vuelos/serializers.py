from rest_framework import serializers
from .models import Vuelo

class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = ['id', 'aerolinea', 'origen', 'destino', 'fecha_salida', 'fecha_entrada', 'precio', 'creado_en']
        read_only_fields = ['creado_en', ]

