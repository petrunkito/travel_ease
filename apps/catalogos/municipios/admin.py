from django.contrib import admin

from apps.catalogos.municipios.models import Municipio

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['id', 'nombre', 'activo']
    exclude = ('eliminado_en',)