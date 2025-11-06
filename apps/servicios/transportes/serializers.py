from rest_framework import serializers
from .models import Transporte

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = ['id', 'origen', 'precio', 'destino', 'creado_en']
        read_only_fields = ['creado_en', ]

