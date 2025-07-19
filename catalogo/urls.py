from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, ServicoViewSet

# Cria um router para registrar os ViewSets
router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet) # A URL será /api/catalogo/produtos/
router.register(r'servicos', ServicoViewSet) # A URL será /api/catalogo/servicos/

urlpatterns = [
    # Inclui as URLs geradas pelo router para os ViewSets
    path('', include(router.urls)),
]

