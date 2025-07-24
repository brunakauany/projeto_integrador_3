from django.db import models
from contas.models import Cliente 

class Pet(models.Model):
    """
    Modelo para representar um Pet.
    Contém informações detalhadas sobre o animal de estimação.
    """
    id = models.BigAutoField(primary_key=True) # ID auto-incrementável
    nome = models.CharField(max_length=255, verbose_name="Nome do Pet")
    tipo = models.CharField(max_length=100, verbose_name="Tipo (Ex: Cachorro, Gato, Pássaro)")
    sexo = models.CharField(max_length=10, verbose_name="Sexo (Ex: Macho, Fêmea)")
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (kg)")
    raca = models.CharField(max_length=100, verbose_name="Raça", blank=True, null=True) # Pode ser opcional
    temperamento = models.TextField(verbose_name="Temperamento do Pet", blank=True, null=True) # Pode ser opcional
    castracao = models.BooleanField(default=False, verbose_name="Castrado(a)?")
    observacoes = models.TextField(verbose_name="Observações Adicionais", blank=True, null=True)

    
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE, 
        related_name='pets',     
        verbose_name="Dono do Pet"
    )

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
        ordering = ['nome'] 

    def __str__(self):
        return f"{self.nome} ({self.tipo} de {self.cliente.nome})"

