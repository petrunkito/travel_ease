from rest_framework import serializers
from .models import Transporte

class TransporteSerializer(serializers.ModelSerializer):
    nombre_tipo_transporte = serializers.CharField(source = "tipo_transporte.nombre", read_only = True)
    class Meta:
        model = Transporte
        fields = ['id', 'tipo_transporte', 'nombre_tipo_transporte', 'origen', 'precio', 'destino', 'creado_en']
        read_only_fields = ['creado_en', ]

