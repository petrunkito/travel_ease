from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'nombre', 'ciudad', 'estrellas', 'precio', 'creado_en']
        read_only_fields = ['creado_en', ]

