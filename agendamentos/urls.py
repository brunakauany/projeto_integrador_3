from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgendamentoViewSet

# Cria um router para registrar o ViewSet
router = DefaultRouter()
router.register(r'agendamentos', AgendamentoViewSet) # A URL será /api/agendamentos/agendamentos/

urlpatterns = [
    # Inclui as URLs geradas pelo router para o AgendamentoViewSet
    path('', include(router.urls)),
]

