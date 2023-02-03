from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView, UpdateView, DetailView, DeleteView

from clinica.models import Paciente

class PacienteList(ListView):
    model = Paciente
    queryset = Paciente.objects.all()

class PacienteCreate(CreateView):
    model = Paciente
    fields = '__all__'
    success_url = reverse_lazy('list')

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = '__all__'
    success_url = reverse_lazy('list')

class PacienteDetail(DetailView):
    model = Paciente
    queryset = Paciente.objects.all()

class PacienteDelete(DeleteView):
    queryset = Paciente.objects.all()
    success_url = reverse_lazy('list')

