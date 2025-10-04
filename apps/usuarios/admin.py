from django.contrib import admin

from apps.usuarios.models import Usuario, Rol, UsuarioRol 

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'codigo', 'descripcion']
    list_display = ['id', 'nombre', 'codigo', 'descripcion', 'creado_en', 'activo']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombres', 'apellidos', 'cedula', 'email', 'telefono']
    list_display = ['id', 'nombres', 'apellidos', 'cedula', 'email', 'telefono']
    exclude = ('last_login', 'first_name', 'last_name','date_joined',  'eliminado_en',)


@admin.register(UsuarioRol)
class UsuarioRolAdmin(admin.ModelAdmin):
    list_display = ['usuario_nombre', 'usuario_apellido', 'rol_nombre']
    
    def usuario_nombre(self, obj):
        return obj.usuario.nombres

    def usuario_apellido(self, obj):
        return obj.usuario.apellidos

    def rol_nombre(self, obj):
        return obj.rol.nombre