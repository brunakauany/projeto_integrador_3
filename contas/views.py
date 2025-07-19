from rest_framework import viewsets
from .models import Cliente, Funcionario, Administrador
from .serializers import ClienteSerializer, FuncionarioSerializer, AdministradorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Cliente.
    Fornece operações CRUD completas para Clientes via API.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Funcionario.
    Fornece operações CRUD completas para Funcionarios via API.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Administrador.
    Fornece operações CRUD completas para Administradores via API.
    """
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

