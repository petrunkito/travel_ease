from django.db import models

# Create your models here.

class HistorialCreacionUsuario(models.Model):
    username = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    usuarioDB = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)

class RegistroSesiones(models.Model):
    nombre_usuario = models.CharField(max_length=255)
    hora_sesion = models.DateTimeField(auto_now_add=True)


class RegistroActividadTablas(models.Model):
    evento_tipo = models.CharField(max_length=255)
    objeto_nombre = models.CharField(max_length=255)
    usuario = models.CharField(max_length=25)



