from django.contrib import admin
from .models import Paciente, Consulta, Medico, Categoria
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Consulta)

