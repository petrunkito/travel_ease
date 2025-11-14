from django.db import models

from apps.seguridad.usuarios.models import DetalleEmpleado, DetalleCliente
from apps.paquetesturisticos.models import PaqueteTuristico
# Create your models here.

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    detalle_empleado = models.ForeignKey(DetalleEmpleado, on_delete=models.PROTECT)
    detalle_cliente = models.ForeignKey(DetalleCliente, on_delete=models.PROTECT)
    
    paquete_turistico = models.ForeignKey(PaqueteTuristico, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    fecha = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)

