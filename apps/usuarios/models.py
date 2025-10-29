from django.db import models
from django.contrib.auth.models import AbstractUser


from apps.municipios.models import Municipio


class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    codigo = models.IntegerField()
    descripcion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

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

class UsuarioRol(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)

    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.usuario.nombres} - {self.usuario.apellidos} - {self.rol.nombre}"

    class Meta:
        unique_together = ('usuario', 'rol')


class Puesto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)



class DetalleEmpleado(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    puesto = models.ForeignKey(Puesto, on_delete=models.PROTECT)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)



class DetalleCliente(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    pasaporte = models.CharField(max_length=50)
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)