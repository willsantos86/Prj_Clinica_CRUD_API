from django.contrib import admin
from django.urls import path, include

from clinica_api.views import CategoriaViewSet, ConsultaViewSet, PacienteViewSet, MedicoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categoria', CategoriaViewSet, basename='api-categoria')
router.register('paciente', PacienteViewSet, basename='api-paciente')
router.register('medico', MedicoViewSet, basename='api-medico')
router.register('consulta', ConsultaViewSet, basename='api-consulta')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinica.urls')),
    path('', include('usuarios.urls')),
    path('', include('router.urls')),
]
