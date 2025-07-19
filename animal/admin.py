from django.contrib import admin
from .models import Pet # Importa o modelo Pet do mesmo app
from contas.models import Cliente # Importa o modelo Cliente para usar nos filtros, se necessário

# Registra o modelo Pet no Django Admin
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de pets no painel de administração
    list_display = ('nome', 'tipo', 'sexo', 'cliente', 'castracao')
    # Define os campos pelos quais será possível pesquisar
    search_fields = ('nome', 'tipo', 'raca', 'cliente__nome') # Permite buscar pelo nome do cliente também
    # Adiciona filtros laterais para facilitar a navegação
    list_filter = ('tipo', 'sexo', 'castracao', 'cliente') # Filtra por tipo, sexo, castração e cliente
    # Adiciona um campo de autocompletar para a chave estrangeira 'cliente'
    # Isso é útil para quando há muitos clientes e evita o carregamento de todos eles
    raw_id_fields = ('cliente',)
# Register your models here.
