from rest_framework import serializers
from .models import Pet
from contas.models import Cliente 

class PetSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Pet.
    Define como os dados do Pet serão representados na API.
    """
    

    class Meta:
        model = Pet
        
        fields = [
            'id', 'nome', 'tipo', 'sexo', 'peso', 'raca',
            'temperamento', 'castracao', 'observacoes', 'cliente'
        ]
        
