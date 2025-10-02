from django.db import models

# Create your models here.

class HistorialCreacionUsuario(models.Model):
    username = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    usuarioDB = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)


