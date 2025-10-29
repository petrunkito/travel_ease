from rest_framework import serializers
from .models import Departamento
from django.db.models import Max 

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['id', 'nombre', 'codigo_departamento', 'creado_en']
        read_only_fields = ['creado_en', 'creado_en','codigo_departamento']

    def create(self, validated_data):
        # calcular automáticamente el código
        ultimo_codigo = Departamento.objects.aggregate(
            max_codigo=Max('codigo_departamento')
        )['max_codigo'] or 0

        validated_data['codigo_departamento'] = ultimo_codigo + 1
        return super().create(validated_data)
