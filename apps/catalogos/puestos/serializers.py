from rest_framework import serializers
from .models import Puesto

class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = ['id', 'nombre', 'creado_en']
        read_only_fields = ['creado_en', ]

    
