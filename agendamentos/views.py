from rest_framework import viewsets
from .models import Agendamento
from .serializers import AgendamentoSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Agendamento.
    Fornece operações CRUD completas para Agendamentos via API.
    """
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

