from django.db import models
from apps.models import Base

class Puesto(Base):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre