from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.models import Base
from apps.catalogos.puestos.models import Puesto


from apps.catalogos.municipios.models import Municipio



class Usuario(Base, AbstractUser):
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, null=True, blank=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    cedula = models.CharField(max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, blank=False) 
    telefono = models.CharField(max_length=50, null=True, blank = True)
    

    REQUIRED_FIELDS = ['nombres', 'apellidos', 'email', 'cedula', 'telefono']

    def __str__(self):
        return f"{self.id} - {self.nombres} - {self.apellidos}"



class DetalleEmpleado(Base):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    puesto = models.ForeignKey(Puesto, on_delete=models.PROTECT)



class DetalleCliente(Base):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    pasaporte = models.CharField(max_length=50)
   