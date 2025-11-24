from django.contrib import admin

# Register your models here.
from apps.catalogos.roles.models import Rol, UsuarioRol


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'codigo', 'descripcion']
    list_display = ['id', 'nombre', 'codigo', 'descripcion', 'creado_en', 'activo']


@admin.register(UsuarioRol)
class UsuarioRolAdmin(admin.ModelAdmin):
    list_display = ['usuario_nombre', 'usuario_apellido', 'rol_nombre']
    
    def usuario_nombre(self, obj):
        return obj.usuario.nombres

    def usuario_apellido(self, obj):
        return obj.usuario.apellidos

    def rol_nombre(self, obj):
        return obj.rol.nombre
    

