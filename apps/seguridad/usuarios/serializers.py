from rest_framework import serializers
from .models import Usuario, DetalleEmpleado, DetalleCliente
from apps.catalogos.puestos.models import Puesto
from django.db import transaction




class UsuarioSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True, validators=[validate_password]  )
    password = serializers.CharField(write_only=True, required=True  )
    confirm_password = serializers.CharField(write_only=True, required=True)
    pasaporte = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(required=True)

    puesto = serializers.PrimaryKeyRelatedField(
        queryset=Puesto.objects.filter(activo=True), #que mande a buscar si el puesto esta activo
        source='id_puesto', # Esto ayuda a mapearlo internamente
        write_only=True, 
        required=False, 
        allow_null=True
    )

    class Meta:
        model = Usuario
        fields = [
            'username', 
            'password', 
            'confirm_password', 
            'nombres',
            'apellidos', 
            'cedula', 
            'email', 
            'telefono',
            'municipio',
            'is_staff',
            'puesto',
            'pasaporte',
        ]

        read_only_fields = ['creado_en', ]

    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        
        if attrs.get('is_staff') is True and not attrs.get('id_puesto'):
             raise serializers.ValidationError({"puesto": "El puesto es requerido para crear un empleado (is_staff=True)."})
        return attrs
    
    def create(self, validated_data):
        # validated_data.pop('confirm_password', None)
        # password = validated_data.pop('password')
        # user = Usuario(**validated_data)
        # user.set_password(password)
        # user.save()
        # return user
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password')
        is_staff = validated_data.pop('is_staff', False)
        puesto_instancia = validated_data.pop('id_puesto', None) # Se llama 'puesto' por el source='puesto' definido arriba
        pasaporte = validated_data.pop('pasaporte', None) 

        # Usamos transaction.atomic para asegurar que se crean LOS DOS o NINGUNO
        with transaction.atomic():
            # 2. Crear el Usuario

            user = Usuario(**validated_data)
            user.set_password(password)
            user.is_staff = is_staff
            user.save()

            # 3. Crear el DetalleEmpleado (Solo si enviaron un puesto)
            if is_staff:
                DetalleEmpleado.objects.create(
                    usuario=user,
                    puesto=puesto_instancia
                )
            else:
                DetalleCliente.objects.create(
                    usuario=user,
                    pasaporte=pasaporte
                )

        return user