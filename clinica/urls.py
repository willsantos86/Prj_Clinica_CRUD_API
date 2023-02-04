from django.urls import path
from .views import PaginaInicial, PacienteCreate, ConsultaCreate, MedicoCreate, CategoriaCreate


urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('clinica/paciente/', PacienteCreate.as_view(), name='cadastrar-paciente'),
    path('clinica/consulta/', ConsultaCreate.as_view(), name='cadastrar-consulta'),
    path('clinica/medico/', MedicoCreate.as_view(), name='cadastrar-medico'),
    path('clinica/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    
]
