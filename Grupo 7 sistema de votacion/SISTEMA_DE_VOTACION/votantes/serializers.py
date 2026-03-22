from rest_framework import serializers
from .models import Votante

class VotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votante
        fields = ['id', 'nombre', 'cedula', 'elecciones']