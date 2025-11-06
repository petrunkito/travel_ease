from django.db import models
from apps.paquetesturisticos.models import PaqueteTuristico
from apps.catalogos.tipotransportes.models import TipoTransportes
from apps.models import Base
# Create your models here.

class Transporte(Base):
    tipo_transporte = models.ForeignKey(TipoTransportes, on_delete=models.PROTECT)
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
   

class ServicioTransporte(models.Model):
    id = models.AutoField(primary_key=True)
    transporte = models.ForeignKey(Transporte, on_delete=models.PROTECT)
    paquete_turistico = models.ForeignKey(PaqueteTuristico, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)