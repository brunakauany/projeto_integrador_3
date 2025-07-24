from django.contrib import admin
from .models import Produto, Servico 
from contas.models import Administrador 

# Registra o modelo Produto no Django Admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'preco', 'quantidade_estoque', 'admin')
    
    search_fields = ('nome', 'descricao', 'admin__nome') 

    list_filter = ('admin', 'quantidade_estoque')
    
    
    raw_id_fields = ('admin',)

# Registra o modelo Servico no Django Admin
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos na lista de serviços
    list_display = ('nome', 'preco', 'duracao_estimada', 'admin')

    search_fields = ('nome', 'descricao', 'admin__nome')
    
    list_filter = ('admin',)
    
    raw_id_fields = ('admin',)


