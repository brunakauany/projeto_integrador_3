from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)


app_name = 'contas'

urlpatterns = [
    
    path('api/', include(router.urls)),

    
    path('cadastro_cliente/', views.cadastrar_cliente, name='cadastro_cliente'),
    path('sucesso/', views.pagina_de_sucesso, name='pagina_de_sucesso'),
]