from rest_framework import serializers
from .models import Municipio
from django.db.models import Max 

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['id', 'nombre', 'codigo_municipio', 'creado_en', 'departamento']
        read_only_fields = ['creado_en',]

    
