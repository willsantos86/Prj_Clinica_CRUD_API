
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Paciente, Consulta, Categoria, Medico

from django.urls import reverse_lazy

################ Create ##################

class PaginaInicial(TemplateView):
    template_name = "clinica/index.html"

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-categoria')

class MedicoCreate(CreateView):
    model = Medico
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-medico')

class PacienteCreate(CreateView):
    model = Paciente
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaCreate(CreateView):
    model = Consulta
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-consulta')

################ Update ##################

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-categoria')

class MedicoUpdate(UpdateView):
    model = Medico
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-medico')

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaUpdate(UpdateView):
    model = Consulta
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-consulta')

################ Delete ##################

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'clinica/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')

class MedicoDelete(DeleteView):
    model = Medico
    template_name = 'clinica/form-excluir.html'
    success_url = reverse_lazy('listar-medico')

class PacienteDelete(DeleteView):
    model = Paciente
    template_name = 'clinica/form-excluir.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaDelete(DeleteView):
    model = Consulta
    template_name = 'clinica/form-excluir.html'
    success_url = reverse_lazy('listar-consulta')

################ Lista ##################

class CategoriaList(ListView):
    model = Categoria
    template_name = 'clinica/lista/categoria.html'

class MedicoList(ListView):
    model = Medico
    template_name = 'clinica/lista/medico.html'

class PacienteList(ListView):
    model = Paciente
    template_name = 'clinica/lista/paciente.html'

class ConsultaList(ListView):
    model = Consulta
    template_name = 'clinica/lista/consulta.html'