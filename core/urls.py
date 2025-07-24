from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static 
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/animal/", include("animal.urls")),
    path("api/catalogo/", include("catalogo.urls")),
    path("api/agendamentos/", include("agendamentos.urls")),
    
    path("", views.home_view, name="home"),
    path("produtos/", views.produtos_view, name="produtos"),
    path("login/", views.login_view, name="login"),

    path('contas/', include('contas.urls')), 

    path('painel_cliente/', views.painel_cliente_view, name='painel_cliente'),
    path('logout/', views.logout_view, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)