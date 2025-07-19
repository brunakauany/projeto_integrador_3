from django.db import models
from contas.models import Cliente, Funcionario, Administrador # Importa os modelos de contas
from animal.models import Pet # Importa o modelo Pet do app clinica_animal (ou animal)

class Agendamento(models.Model):
    """
    Modelo para representar um Agendamento.
    Conecta clientes, pets, funcionários e administradores para um serviço ou evento.
    """
    id = models.BigAutoField(primary_key=True) # ID auto-incrementável
    data_hora = models.DateTimeField(verbose_name="Data e Hora do Agendamento")
    status = models.CharField(
        max_length=50,
        verbose_name="Status do Agendamento",
        default='Pendente', # Define um status padrão
        choices=[
            ('Pendente', 'Pendente'),
            ('Confirmado', 'Confirmado'),
            ('Cancelado', 'Cancelado'),
            ('Concluído', 'Concluído'),
        ]
    )
    observacoes = models.TextField(verbose_name="Observações", blank=True, null=True)

    # Chaves estrangeiras conforme o diagrama
    pet = models.ForeignKey(
        Pet,
        on_delete=models.PROTECT, # Protege o agendamento de ser deletado se o Pet for removido
        related_name='agendamentos',
        verbose_name="Pet Agendado"
    )
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.PROTECT, # Protege o agendamento de ser deletado se o Funcionário for removido
        related_name='agendamentos_funcionario',
        verbose_name="Funcionário Responsável"
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT, # Protege o agendamento de ser deletado se o Cliente for removido
        related_name='agendamentos_cliente',
        verbose_name="Cliente do Agendamento"
    )
    admin = models.ForeignKey(
        Administrador,
        on_delete=models.PROTECT, # Protege o agendamento de ser deletado se o Administrador for removido
        related_name='agendamentos_admin',
        verbose_name="Administrador que Registrou"
    )

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        ordering = ['data_hora'] # Ordena os agendamentos pela data e hora por padrão

    def __str__(self):
        return f"Agendamento para {self.pet.nome} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

# Create your models here.
