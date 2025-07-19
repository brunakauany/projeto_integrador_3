from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, FuncionarioViewSet, AdministradorViewSet

# Cria um router para registrar os ViewSets
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'administradores', AdministradorViewSet)

urlpatterns = [
    # Inclui as URLs geradas pelo router para os ViewSets
    path('', include(router.urls)),
]

