from rest_framework import viewsets
from .models import Pet
from .serializers import PetSerializer

class PetViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Pet.
    Fornece operações CRUD completas para Pets via API.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

