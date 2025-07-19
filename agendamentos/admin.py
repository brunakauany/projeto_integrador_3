from django.contrib import admin
from .models import Agendamento # Importa o modelo Agendamento do mesmo app
from contas.models import Cliente, Funcionario, Administrador # Importa modelos relacionados para filtros/exibição
from animal.models import Pet # Importa modelo Pet para filtros/exibição

# Registra o modelo Agendamento no Django Admin
@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de agendamentos no painel de administração
    list_display = ('data_hora', 'pet', 'cliente', 'funcionario', 'status', 'admin')
    # Define os campos pelos quais será possível pesquisar
    search_fields = (
        'pet__nome',        # Busca pelo nome do pet
        'cliente__nome',    # Busca pelo nome do cliente
        'funcionario__nome', # Busca pelo nome do funcionário
        'status',
        'observacoes'
    )
    # Adiciona filtros laterais para facilitar a navegação
    list_filter = ('status', 'data_hora', 'funcionario', 'cliente', 'pet')
    # Adiciona um campo de autocompletar para as chaves estrangeiras
    # Isso é útil para quando há muitos registros e evita o carregamento de todos eles
    raw_id_fields = ('pet', 'funcionario', 'cliente', 'admin')
    # Define a ordem padrão dos resultados
    ordering = ('-data_hora',) # Ordena do mais recente para o mais antigo

# Register your models here.
