from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet

# Cria um router para registrar o ViewSet
router = DefaultRouter()
router.register(r'pets', PetViewSet) # A URL será /api/animais/pets/

urlpatterns = [
    # Inclui as URLs geradas pelo router para o PetViewSet
    path('', include(router.urls)),
]

