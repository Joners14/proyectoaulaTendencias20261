from django.db import models
from elecciones.models import Eleccion

class Votante(models.Model):
    nombre   = models.CharField(max_length=100)
    cedula   = models.CharField(max_length=20, unique=True)
    elecciones = models.ManyToManyField(Eleccion, related_name='votantes_habilitados')

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"