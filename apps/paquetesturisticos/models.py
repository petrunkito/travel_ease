from django.db import models

from apps.usuarios.models import DetalleEmpleado
# Create your models here.

class PaqueteTuristico(models.Model):
    id = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(DetalleEmpleado, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    total_precio = models.DecimalField(max_digits=12, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)
