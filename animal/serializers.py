from rest_framework import serializers
from .models import Pet
from contas.models import Cliente # Precisamos do Cliente para o campo ForeignKey

class PetSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Pet.
    Define como os dados do Pet serão representados na API.
    """
    # Para exibir o nome do cliente em vez do ID, podemos usar StringRelatedField
    # ou um serializer aninhado se mais detalhes do cliente forem necessários.
    # Por enquanto, vamos manter o padrão que mostra o ID do cliente, ou o nome se o cliente tiver __str__ definido.
    # Se quiser mostrar o nome do cliente, descomente a linha abaixo e comente a linha 'cliente' no fields.
    # cliente_nome = serializers.ReadOnlyField(source='cliente.nome')

    class Meta:
        model = Pet
        # Inclui todos os campos do modelo Pet
        fields = [
            'id', 'nome', 'tipo', 'sexo', 'peso', 'raca',
            'temperamento', 'castracao', 'observacoes', 'cliente'
        ]
        # Se você quiser que o campo 'cliente' seja representado pelo nome do cliente na leitura,
        # mas ainda aceite o ID do cliente na escrita, você precisaria de um SerializerMethodField
        # ou ajustar o campo 'cliente' diretamente. Por padrão, ele aceitará o ID.

