from django.db import models
from apps.models import Base

# Create your models here.

class Departamento(Base):
    nombre = models.CharField(max_length=255, unique=True)
    codigo_departamento = models.CharField(unique=True, max_length=15)   

    def __str__(self):
        return f"{self.codigo_departamento} - {self.nombre}"

