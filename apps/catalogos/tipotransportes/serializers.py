from rest_framework import serializers
from .models import TipoTransportes

class TipoTransportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTransportes
        fields = ['id', 'nombre',  'creado_en']
        read_only_fields = ['creado_en',]

    
