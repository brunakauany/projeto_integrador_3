from rest_framework import serializers
from .models import Produto, Servico
from contas.models import Administrador # Precisamos do Administrador para o campo ForeignKey

class ProdutoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Produto.
    Define como os dados do Produto serão representados na API.
    """
    # Para exibir o nome do administrador em vez do ID, podemos usar StringRelatedField
    # ou um serializer aninhado se mais detalhes do administrador forem necessários.
    # admin_nome = serializers.ReadOnlyField(source='admin.nome') # Exemplo de como exibir o nome do admin

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
    # admin_nome = serializers.ReadOnlyField(source='admin.nome') # Exemplo de como exibir o nome do admin

    class Meta:
        model = Servico
        # Inclui todos os campos do modelo Servico
        fields = [
            'id', 'nome', 'descricao', 'preco', 'duracao_estimada', 'admin'
        ]

