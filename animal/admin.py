from django.contrib import admin
from .models import Pet 
from contas.models import Cliente 

# Registra o modelo Pet no Django Admin
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'tipo', 'sexo', 'cliente', 'castracao')
    
    search_fields = ('nome', 'tipo', 'raca', 'cliente__nome') 

    list_filter = ('tipo', 'sexo', 'castracao', 'cliente') 
   
    raw_id_fields = ('cliente',)

