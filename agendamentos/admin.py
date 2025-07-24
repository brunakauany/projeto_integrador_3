from django.contrib import admin
from .models import Agendamento # Importa o modelo Agendamento do mesmo app
from contas.models import Cliente, Funcionario, Administrador # Importa modelos relacionados para filtros/exibição
from animal.models import Pet # Importa modelo Pet para filtros/exibição

# Registra o modelo Agendamento no Django Admin
@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    
    list_display = ('data_hora', 'pet', 'cliente', 'funcionario', 'status', 'admin')
    
    search_fields = (
        'pet__nome',        
        'cliente__nome',    
        'funcionario__nome', 
        'status',
        'observacoes'
    )
    # Adiciona filtros laterais para facilitar a navegação
    list_filter = ('status', 'data_hora', 'funcionario', 'cliente', 'pet')
    
    raw_id_fields = ('pet', 'funcionario', 'cliente', 'admin')
    
    ordering = ('-data_hora',) 


