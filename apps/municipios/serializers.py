from rest_framework import serializers
from .models import Municipio
from django.db.models import Max 

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['id', 'nombre', 'codigo_municipio', 'creado_en', 'departamento']
        read_only_fields = ['creado_en','codigo_municipio', ]

    def create(self, validated_data):
        # calcular automáticamente el código
        ultimo_codigo = Municipio.objects.aggregate(
            max_codigo=Max('codigo_municipio')
        )['max_codigo'] or 0

        validated_data['codigo_municipio'] = ultimo_codigo + 1
        return super().create(validated_data)
