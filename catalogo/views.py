from rest_framework import viewsets
from .models import Produto, Servico
from .serializers import ProdutoSerializer, ServicoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Produto.
    Fornece operações CRUD completas para Produtos via API.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Servico.
    Fornece operações CRUD completas para Servicos via API.
    """
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

