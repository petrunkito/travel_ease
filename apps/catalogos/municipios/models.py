from django.db import models
from apps.models import Base
from apps.catalogos.departamentos.models import Departamento

# Create your models here.
class Municipio(Base):
    codigo_municipio = models.CharField(unique=True, max_length=15)
    nombre = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.codigo_municipio} - {self.nombre}"

