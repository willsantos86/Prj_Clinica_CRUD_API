
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView

from .models import Paciente, Consulta, Categoria, Medico

from django.urls import reverse_lazy

################ Create ##################

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

    ################ Update ##################

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('inicio')

class MedicoUpdate(UpdateView):
    model = Medico
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('inicio')

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('inicio')

class ConsultaUpdate(UpdateView):
    model = Consulta
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('inicio')