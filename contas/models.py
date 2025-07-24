from django.db import models
from django.contrib.auth.hashers import make_password 

class Pessoa(models.Model):
    """
    Modelo abstrato que define campos comuns para Cliente, Funcionario e Administrador.
    Não será criada uma tabela separada para Pessoa no banco de dados.
    """
    id = models.BigAutoField(primary_key=True) 
    nome = models.CharField(max_length=255, verbose_name="Nome Completo")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(unique=True, verbose_name="Email")
    senha = models.CharField(max_length=128, verbose_name="Senha Hash") 

    class Meta:
        abstract = True 
    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para fazer o hash da senha antes de salvar.
        """
        
        if not self.pk or self._state.adding: 
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Cliente(Pessoa):
    """
    Modelo para representar um Cliente.
    Herda campos comuns de Pessoa.
    """
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    endereco = models.TextField(verbose_name="Endereço Completo")

    class Meta:
        verbose_name = "Conta de Cliente"
        verbose_name_plural = "Contas de Clientes"

class Funcionario(Pessoa):
    """
    Modelo para representar um Funcionário.
    Herda campos comuns de Pessoa.
    """
    cargo = models.CharField(max_length=100, verbose_name="Cargo")

    class Meta:
        verbose_name = "Conta de Funcionário"
        verbose_name_plural = "Contas de Funcionários"

class Administrador(Pessoa):
    """
    Modelo para representar um Administrador.
    Herda campos comuns de Pessoa.
    """
  
    class Meta:
        verbose_name = "Conta de Administrador"
        verbose_name_plural = "Contas de Administradores"


