from django.db import models
from apps.departamentos.models import Departamento

# Create your models here.
class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_municipio = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.codigo_municipio} - {self.nombre}"

