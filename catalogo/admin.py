from django.contrib import admin
from .models import Produto, Servico # Importa os modelos Produto e Servico do mesmo app
from contas.models import Administrador # Importa o modelo Administrador para usar nos filtros/exibição

# Registra o modelo Produto no Django Admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de produtos no painel de administração
    list_display = ('nome', 'preco', 'quantidade_estoque', 'admin')
    # Define os campos pelos quais será possível pesquisar
    search_fields = ('nome', 'descricao', 'admin__nome') # Permite buscar pelo nome do administrador também
    # Adiciona filtros laterais para facilitar a navegação
    list_filter = ('admin', 'quantidade_estoque')
    # Adiciona um campo de autocompletar para a chave estrangeira 'admin'
    # Isso é útil para quando há muitos administradores e evita o carregamento de todos eles
    raw_id_fields = ('admin',)

# Registra o modelo Servico no Django Admin
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de serviços
    list_display = ('nome', 'preco', 'duracao_estimada', 'admin')
    # Define os campos pelos quais será possível pesquisar
    search_fields = ('nome', 'descricao', 'admin__nome') # Permite buscar pelo nome do administrador também
    # Adiciona filtros laterais para o campo 'admin'
    list_filter = ('admin',)
    # Adiciona um campo de autocompletar para a chave estrangeira 'admin'
    raw_id_fields = ('admin',)


# Register your models here.
