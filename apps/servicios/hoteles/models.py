from django.db import models

from apps.paquetesturisticos.models import PaqueteTuristico
# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estrellas = models.IntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)



class ServicioHotel(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    paquete_turistico = models.ForeignKey(PaqueteTuristico, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)