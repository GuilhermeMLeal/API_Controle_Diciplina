# Generated by Django 4.2.5 on 2023-09-20 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlunoEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TarefaEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('data_entrega', models.DateField()),
                ('concluida', models.BooleanField(default=False)),
                ('tarefa_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_controle_disciplina.alunoentity')),
                ('tarefa_disciplina', models.ManyToManyField(to='api_controle_disciplina.disciplinaentity')),
            ],
        ),
    ]
