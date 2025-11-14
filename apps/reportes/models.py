from django.db import models
from apps.catalogos.departamentos.models import Departamento
from apps.seguridad.usuarios.models import DetalleCliente, DetalleEmpleado
from apps.reservas.models import Reserva

# Create your models here.
class ReporteVentasDiarias(models.Model):
    nombre_cliente = models.CharField(max_length=255)
    nombre_empleado = models.CharField(max_length=255)
    nombre_paquete_turistico = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    detalle_cliente = models.ForeignKey(DetalleCliente, on_delete=models.PROTECT)
    detalle_empleado = models.ForeignKey(DetalleEmpleado, on_delete=models.PROTECT)
    reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT)
    creado_en = models.DateTimeField(auto_now_add=True)

    




