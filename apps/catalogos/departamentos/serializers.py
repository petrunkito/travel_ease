from rest_framework import serializers
from .models import Departamento
from django.db.models import Max 

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['id', 'nombre', 'codigo_departamento', 'creado_en']
        read_only_fields = ['creado_en', ]

    
