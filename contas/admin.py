from django.contrib import admin
from .models import Cliente, Funcionario, Administrador


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
   
    list_display = ('nome', 'email', 'telefone', 'cpf')
    
    search_fields = ('nome', 'email', 'cpf')
   
    list_filter = ('nome',)

# Registra o modelo Funcionario no Django Admin
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'email', 'telefone', 'cargo')
    
    search_fields = ('nome', 'email', 'cargo')
   
    list_filter = ('cargo',)


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'email', 'telefone')
    
    search_fields = ('nome', 'email')

# Register your models here.
