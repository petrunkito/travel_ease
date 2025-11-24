from rest_framework import serializers
from .models import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre', 'codigo', 'descripcion', 'creado_en']
        read_only_fields = ['creado_en', ]

    
