from django.db import models
from contas.models import Administrador # Importa o modelo Administrador do app 'contas'

class Produto(models.Model):
    """
    Modelo para representar um Produto.
    Contém informações sobre itens que podem ser vendidos.
    """
    id = models.BigAutoField(primary_key=True) # ID auto-incrementável
    nome = models.CharField(max_length=255, verbose_name="Nome do Produto")
    descricao = models.TextField(verbose_name="Descrição do Produto", blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Unitário")
    quantidade_estoque = models.IntegerField(verbose_name="Quantidade em Estoque")

    
    admin = models.ForeignKey(
        Administrador,
        on_delete=models.SET_NULL, 
        related_name='produtos_gerenciados', 
        verbose_name="Administrador Responsável",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome'] 

    def __str__(self):
        return self.nome

class Servico(models.Model):
    """
    Modelo para representar um Serviço.
    Contém informações sobre os serviços oferecidos.
    """
    id = models.BigAutoField(primary_key=True) # ID auto-incrementável
    nome = models.CharField(max_length=255, verbose_name="Nome do Serviço")
    descricao = models.TextField(verbose_name="Descrição do Serviço", blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço do Serviço")
    duracao_estimada = models.DurationField(verbose_name="Duração Estimada") # Campo para duração (ex: 1h30m)

    
    admin = models.ForeignKey(
        Administrador,
        on_delete=models.SET_NULL, 
        related_name='servicos_gerenciados', 
        verbose_name="Administrador Responsável",
        null=True, 
        blank=True 
    )

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ['nome'] # Ordena os serviços pelo nome por padrão

    def __str__(self):
        return self.nome
