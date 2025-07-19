from django.contrib import admin
from .models import Cliente, Funcionario, Administrador

# Registra o modelo Cliente no Django Admin
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de clientes no painel de administração
    list_display = ('nome', 'email', 'telefone', 'cpf')
    # Define os campos pelos quais será possível pesquisar
    search_fields = ('nome', 'email', 'cpf')
    # Adiciona filtros laterais para facilitar a navegação
    list_filter = ('nome',)

# Registra o modelo Funcionario no Django Admin
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de funcionários
    list_display = ('nome', 'email', 'telefone', 'cargo')
    # Define os campos pelos quais será possível pesquisar
    search_fields = ('nome', 'email', 'cargo')
    # Adiciona filtros laterais para o campo 'cargo'
    list_filter = ('cargo',)

# Registra o modelo Administrador no Django Admin
@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de administradores
    list_display = ('nome', 'email', 'telefone')
    # Define os campos pelos quais será possível pesquisar
    search_fields = ('nome', 'email')

# Register your models here.
