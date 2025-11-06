from django.db import models
from apps.models import Base

class TipoTransportes(Base):
    nombre = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.nombre}"

