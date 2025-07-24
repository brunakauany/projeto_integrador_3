from rest_framework import serializers
from .models import Agendamento
from contas.serializers import ClienteSerializer, FuncionarioSerializer, AdministradorSerializer
from animal.serializers import PetSerializer

class AgendamentoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Agendamento.
    Define como os dados do Agendamento serão representados na API.
    """
    
    pet = PetSerializer(read_only=True)
    funcionario = FuncionarioSerializer(read_only=True)
    cliente = ClienteSerializer(read_only=True)
    admin = AdministradorSerializer(read_only=True)

    
    pet_id = serializers.PrimaryKeyRelatedField(
        queryset=PetSerializer.Meta.model.objects.all(), source='pet', write_only=True
    )
    funcionario_id = serializers.PrimaryKeyRelatedField(
        queryset=FuncionarioSerializer.Meta.model.objects.all(), source='funcionario', write_only=True
    )
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=ClienteSerializer.Meta.model.objects.all(), source='cliente', write_only=True
    )
    admin_id = serializers.PrimaryKeyRelatedField(
        queryset=AdministradorSerializer.Meta.model.objects.all(), source='admin', write_only=True
    )

    class Meta:
        model = Agendamento
        # Inclui todos os campos do modelo Agendamento,
        # e os campos de ID para escrita de chaves estrangeiras.
        fields = [
            'id', 'data_hora', 'status', 'observacoes',
            'pet', 'funcionario', 'cliente', 'admin', 
            'pet_id', 'funcionario_id', 'cliente_id', 'admin_id' 
        ]

