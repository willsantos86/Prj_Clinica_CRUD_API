
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .models import Paciente, Consulta, Categoria, Medico

from django.urls import reverse_lazy



class PaginaInicial(TemplateView):
    template_name = "clinica/index.html"

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('inicio')

class MedicoCreate(CreateView):
    model = Medico
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('inicio')

class PacienteCreate(CreateView):
    model = Paciente
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('inicio')

class ConsultaCreate(CreateView):
    model = Consulta
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('inicio')