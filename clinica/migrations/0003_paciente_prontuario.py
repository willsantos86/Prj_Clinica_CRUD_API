# Generated by Django 4.1.6 on 2023-02-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_consulta_observacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='prontuario',
            field=models.TextField(default='Sem registros', verbose_name='Prontuário'),
        ),
    ]
