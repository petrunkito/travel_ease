from django.db import models
from apps.models import Base
from apps.seguridad.usuarios.models import Usuario

# Create your models here.




class Rol(Base):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(unique=True, max_length=15)  
    descripcion = models.TextField()   

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    


class UsuarioRol(Base):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.usuario.nombres} - {self.usuario.apellidos} - {self.rol.nombre}"

    class Meta:
        unique_together = ('usuario', 'rol')
