from django.db import models

from apps.paquetesturisticos.models import PaqueteTuristico
# Create your models here.


class TipoTransporte(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)



class Transporte(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_transporte = models.ForeignKey(TipoTransporte, on_delete=models.PROTECT)
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)



class ServicioTransporte(models.Model):
    id = models.AutoField(primary_key=True)
    transporte = models.ForeignKey(Transporte, on_delete=models.PROTECT)
    paquete_turistico = models.ForeignKey(PaqueteTuristico, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)