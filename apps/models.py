from django.db import models


class Base(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    eliminado_en = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    class Meta:
        abstract=True
