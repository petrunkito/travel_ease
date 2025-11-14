from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.models import Base
from apps.catalogos.puestos.models import Puesto


from apps.catalogos.municipios.models import Municipio


class Rol(Base):
    nombre = models.CharField(max_length=255)
    codigo = models.IntegerField()
    descripcion = models.TextField()   

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, null=True, blank=True) 
 
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    cedula = models.CharField(max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, blank=False) # Ya está bien como campo principal
    telefono = models.CharField(max_length=50, null=True, blank = True)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['nombres', 'apellidos', 'email', 'cedula', 'telefono']

    def __str__(self):
        return f"{self.id} - {self.nombres} - {self.apellidos}"

class UsuarioRol(Base):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.usuario.nombres} - {self.usuario.apellidos} - {self.rol.nombre}"

    class Meta:
        unique_together = ('usuario', 'rol')


class DetalleEmpleado(Base):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    puesto = models.ForeignKey(Puesto, on_delete=models.PROTECT)



class DetalleCliente(Base):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    pasaporte = models.CharField(max_length=50)
   