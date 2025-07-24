from rest_framework import serializers
from .models import Produto, Servico
from contas.models import Administrador 

class ProdutoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Produto.
    Define como os dados do Produto serão representados na API.
    """
   

    class Meta:
        model = Produto
        # Inclui todos os campos do modelo Produto
        fields = [
            'id', 'nome', 'descricao', 'preco', 'quantidade_estoque', 'admin'
        ]

class ServicoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Servico.
    Define como os dados do Servico serão representados na API.
    """
    

    class Meta:
        model = Servico
        # Inclui todos os campos do modelo Servico
        fields = [
            'id', 'nome', 'descricao', 'preco', 'duracao_estimada', 'admin'
        ]

