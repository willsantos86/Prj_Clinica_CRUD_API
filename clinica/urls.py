from django.urls import path
from .views import PaginaInicial, PacienteCreate, ConsultaCreate, MedicoCreate, CategoriaCreate
from .views import PacienteUpdate, ConsultaUpdate, MedicoUpdate, CategoriaUpdate


urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('clinica/paciente/', PacienteCreate.as_view(), name='cadastrar-paciente'),
    path('clinica/consulta/', ConsultaCreate.as_view(), name='cadastrar-consulta'),
    path('clinica/medico/', MedicoCreate.as_view(), name='cadastrar-medico'),
    path('clinica/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),

    path('editar/paciente/<int:pk>/',PacienteUpdate.as_view(),name='editar-paciente'),
    path('editar/consulta/<int:pk>/',ConsultaUpdate.as_view(),name='editar-consulta'),
    path('editar/medico/<int:pk>/',MedicoUpdate.as_view(),name='editar-medico'),
    path('editar/categoria/<int:pk>/',CategoriaUpdate.as_view(),name='editar-categoria'),
    
]
