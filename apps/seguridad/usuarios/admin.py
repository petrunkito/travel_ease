from django.contrib import admin


from apps.seguridad.usuarios.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombres', 'apellidos', 'cedula', 'email', 'telefono']
    list_display = ['id', 'nombres', 'apellidos', 'cedula', 'email', 'telefono']
    exclude = ('last_login', 'first_name', 'last_name','date_joined',  'eliminado_en',)



