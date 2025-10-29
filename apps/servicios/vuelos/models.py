from django.db import models
from apps.paquetesturisticos.models import PaqueteTuristico

# Create your models here.

class Vuelo(models.Model):
    id = models.AutoField(primary_key=True)
    aerolinea = models.CharField(max_length=255)
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    fecha_salida = models.DateField()
    fecha_entrada = models.DateField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    


class ServicioVuelo(models.Model):
    id = models.AutoField(primary_key=True)
    vuelo = models.ForeignKey(Vuelo, on_delete=models.PROTECT)
    paquete_turistico = models.ForeignKey(PaqueteTuristico, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)