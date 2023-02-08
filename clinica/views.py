
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Paciente, Consulta, Categoria, Medico

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

################ Create ##################

class PaginaInicial(TemplateView):
    template_name = "clinica/index.html"

class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'Administrador'
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-categoria')

class MedicoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u'Administrador' 
    model = Medico
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-medico')

class PacienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Paciente
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
   
    model = Consulta
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-consulta')

################ Update ##################

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-categoria')

class MedicoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Medico
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-medico')

class PacienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Paciente
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaUpdate(LoginRequiredMixin, UpdateView):
    
    model = Consulta
    fields = '__all__'
    template_name = 'clinica/form.html'
    success_url = reverse_lazy('listar-consulta')

################ Delete ##################

class CategoriaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'clinica/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')

class MedicoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Medico
    template_name = 'clinica/form-excluir.html'
    success_url = reverse_lazy('listar-medico')

class PacienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Paciente
    template_name = 'clinica/form-excluir.html'
    success_url = reverse_lazy('listar-paciente')

class ConsultaDelete(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Consulta
    template_name = 'clinica/form-excluir.html'
    success_url = reverse_lazy('listar-consulta')

################ Lista ##################

class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'clinica/lista/categoria.html'

class MedicoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Medico
    template_name = 'clinica/lista/medico.html'

class PacienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Paciente
    template_name = 'clinica/lista/paciente.html'
    

class ConsultaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Consulta
    template_name = 'clinica/lista/consulta.html'