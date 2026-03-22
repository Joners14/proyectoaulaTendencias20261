from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Votante
from .serializers import VotanteSerializer

class VotanteViewSet(ModelViewSet):
    queryset = Votante.objects.all()
    serializer_class = VotanteSerializer

    @action(detail=False, methods=['get'], url_path='por-eleccion/(?P<eleccion_id>[^/.]+)')
    def por_eleccion(self, request, eleccion_id=None):
        votantes = Votante.objects.filter(elecciones__id=eleccion_id)
        serializer = self.get_serializer(votantes, many=True)
        return Response(serializer.data)