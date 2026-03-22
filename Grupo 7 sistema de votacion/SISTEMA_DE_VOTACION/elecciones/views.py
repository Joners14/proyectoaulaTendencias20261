from rest_framework.viewsets import ModelViewSet
from .models import Eleccion
from .serializers import EleccionSerializer

class EleccionViewSet(ModelViewSet):
    queryset = Eleccion.objects.all()
    serializer_class = EleccionSerializer