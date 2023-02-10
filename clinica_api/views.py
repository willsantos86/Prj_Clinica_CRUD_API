from rest_framework import viewsets
from clinica.models import Categoria, Consulta, Paciente, Medico
from serializer import CategoriaSerializer, ConsultaSerializer, PacienteSerializer, MedicoSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as consultas"""
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as categorias(especialidades)"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    """Exibindo todas os pacientes"""
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os medicos"""
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer