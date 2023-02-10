from django.urls import path
from .views import PaginaInicial
from .views import PacienteCreate, ConsultaCreate, MedicoCreate, CategoriaCreate
from .views import PacienteUpdate, ConsultaUpdate, MedicoUpdate, CategoriaUpdate
from .views import PacienteDelete, ConsultaDelete, MedicoDelete, CategoriaDelete
from .views import PacienteList, ConsultaList, MedicoList, CategoriaList



urlpatterns = [
    path('inicio/', PaginaInicial.as_view(), name='inicio'),
    path('clinica/paciente/', PacienteCreate.as_view(), name='cadastrar-paciente'),
    path('clinica/consulta/', ConsultaCreate.as_view(), name='cadastrar-consulta'),
    path('clinica/medico/', MedicoCreate.as_view(), name='cadastrar-medico'),
    path('clinica/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),

    path('editar/paciente/<int:pk>/', PacienteUpdate.as_view(),name='editar-paciente'),
    path('editar/consulta/<int:pk>/', ConsultaUpdate.as_view(),name='editar-consulta'),
    path('editar/medico/<int:pk>/', MedicoUpdate.as_view(),name='editar-medico'),
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(),name='editar-categoria'),

    path('excluir/paciente/<int:pk>/' ,PacienteDelete.as_view(),name='excluir-paciente'),
    path('excluir/consulta/<int:pk>/', ConsultaDelete.as_view(),name='excluir-consulta'),
    path('excluir/medico/<int:pk>/', MedicoDelete.as_view(),name='excluir-medico'),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(),name='excluir-categoria'),

    path('listar/paciente/', PacienteList.as_view(), name='listar-paciente'),
    path('listar/consulta/', ConsultaList.as_view(), name='listar-consulta'),
    path('listar/medico/', MedicoList.as_view(), name='listar-medico'),
    path('listar/categoria/', CategoriaList.as_view(), name='listar-categoria'),

    
    
]
