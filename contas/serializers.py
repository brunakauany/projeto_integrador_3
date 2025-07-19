from rest_framework import serializers
from .models import Cliente, Funcionario, Administrador

class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Cliente.
    Define como os dados do Cliente serão representados na API.
    """
    class Meta:
        model = Cliente
        # Inclui todos os campos do modelo Cliente, exceto a senha para leitura
        # A senha será tratada separadamente na criação/atualização
        fields = ['id', 'nome', 'telefone', 'email', 'cpf', 'endereco']
        # Define 'senha' como write_only para que não seja retornada nas respostas GET
        extra_kwargs = {'senha': {'write_only': True}}

    def create(self, validated_data):
        """
        Sobrescreve o método create para garantir que a senha seja hashed
        ao criar um novo Cliente via API.
        """
        # O método save do modelo Pessoa já faz o hash da senha,
        # então basta chamar o create padrão.
        return Cliente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Sobrescreve o método update para garantir que a senha seja hashed
        ao atualizar um Cliente via API, se ela for fornecida.
        """
        # Se a senha for fornecida nos dados de atualização, atualiza-a
        if 'senha' in validated_data:
            instance.senha = validated_data.pop('senha')
            instance.save() # Chama o save do modelo para aplicar o hash
        # Atualiza os outros campos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class FuncionarioSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Funcionario.
    Define como os dados do Funcionario serão representados na API.
    """
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'telefone', 'email', 'cargo']
        extra_kwargs = {'senha': {'write_only': True}}

    def create(self, validated_data):
        return Funcionario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'senha' in validated_data:
            instance.senha = validated_data.pop('senha')
            instance.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class AdministradorSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Administrador.
    Define como os dados do Administrador serão representados na API.
    """
    class Meta:
        model = Administrador
        fields = ['id', 'nome', 'telefone', 'email']
        extra_kwargs = {'senha': {'write_only': True}}

    def create(self, validated_data):
        return Administrador.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'senha' in validated_data:
            instance.senha = validated_data.pop('senha')
            instance.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance