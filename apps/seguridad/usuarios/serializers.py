from rest_framework import serializers
from .models import Usuario
from django.db.models import Max 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'codigo_departamento', 'creado_en']
        read_only_fields = ['creado_en', ]

    
