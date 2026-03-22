from django.db import models
from elecciones.models import Eleccion

class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    eleccion = models.ForeignKey(Eleccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre