# Generated by Django 4.0.4 on 2022-05-26 01:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)])),
                ('Etcs', models.IntegerField()),
                ('topicos', models.CharField(max_length=100)),
                ('ranking', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('ano_letivo', models.CharField(max_length=10)),
                ('link', models.URLField(blank=True)),
                ('imagem', models.ImageField(default='', upload_to='cadeiras/')),
            ],
        ),
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('referencia', models.CharField(max_length=30)),
                ('periodo', models.IntegerField()),
                ('empresa', models.CharField(max_length=30)),
                ('formador', models.URLField()),
                ('ficheiro', models.FileField(upload_to='formadores/')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('local', models.ImageField(upload_to='escolas/')),
                ('logo', models.ImageField(upload_to='escolas/')),
                ('nome_curso', models.CharField(max_length=70)),
                ('tipo_ensino', models.CharField(max_length=30)),
                ('periodo', models.CharField(max_length=30)),
                ('morada', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='interesses/')),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('certificado', models.URLField(blank=True)),
                ('compreensao', models.CharField(max_length=2)),
                ('conversacao', models.CharField(max_length=2)),
                ('escrita', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('texto', models.TextField()),
                ('imagem', models.ImageField(upload_to='noticias/')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkdln', models.URLField()),
                ('link_professor', models.URLField(blank=True)),
                ('nome', models.CharField(max_length=20)),
                ('link_aluno', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('apelido', models.CharField(max_length=30)),
                ('pontuacao', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=30)),
                ('data', models.DateField()),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=50)),
                ('link', models.URLField(blank=True)),
                ('imagem', models.ImageField(blank=True, upload_to='posts/')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('acronimo', models.CharField(max_length=5)),
                ('ano', models.IntegerField()),
                ('criador', models.CharField(max_length=30)),
                ('logotipo', models.ImageField(upload_to='tecnologias/')),
                ('link', models.URLField()),
                ('descricao', models.CharField(max_length=100)),
                ('BackEnd', models.BooleanField(default=False)),
                ('FrontEnd', models.BooleanField(default=False)),
                ('Outra', models.BooleanField(default=False)),
                ('codigo', models.ImageField(blank=True, upload_to='codigos/')),
            ],
        ),
        migrations.CreateModel(
            name='TrabalhoCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('ano', models.IntegerField()),
                ('resumo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=500)),
                ('github', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('relatorio', models.FileField(upload_to='trabalhos/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa')),
                ('orientador', models.ManyToManyField(related_name='Orientador', to='portfolio.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=500)),
                ('imagem', models.ImageField(upload_to='projetos/')),
                ('ano', models.IntegerField()),
                ('github', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('participantes', models.ManyToManyField(to='portfolio.pessoa')),
                ('tecnologias', models.ManyToManyField(blank=True, to='portfolio.tecnologia')),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=100)),
                ('cadeira', models.ManyToManyField(blank=True, to='portfolio.cadeira')),
                ('projeto', models.ManyToManyField(blank=True, to='portfolio.projeto')),
            ],
        ),
        migrations.AddField(
            model_name='cadeira',
            name='professor',
            field=models.ManyToManyField(to='portfolio.pessoa'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.projeto'),
        ),
    ]
