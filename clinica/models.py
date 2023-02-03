from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=30, verbose_name='Especialidade')
    def __str__(self):
        return self.nome_categoria

class Medico(models.Model):
    nome_medico = models.CharField(max_length=50, verbose_name='Nome')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, verbose_name='Especialidade')
    matricula = models.CharField(max_length=30)
    def __str__(self):
        return self.nome_medico

class Paciente(models.Model):
    Lista_genero = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outros', 'Outros'),
    )
    nome_paciente = models.CharField(max_length=50, verbose_name='Nome Paciente')
    tel = models.CharField(max_length=14, verbose_name='Telefone')
    genero = models.CharField(max_length=10, verbose_name='Gênero', choices=Lista_genero)
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data Nascimento')
    def __str__(self):
        return self.nome_paciente

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Paciente')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Especialidade')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Médico')
    data = models.DateField()
    def __str__(self):
        return f'{self.paciente} - {self.medico} - {self.categoria}'