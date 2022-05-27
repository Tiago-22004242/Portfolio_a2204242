from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Post(models.Model):
    autor = models.CharField(max_length=30)
    data = models.DateField()
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='posts/',blank=True)
    def __str__(self):
        return self.titulo

class Escola(models.Model):
    nome = models.CharField(max_length=50)
    local = models.ImageField(upload_to='escolas/')
    logo = models.ImageField(upload_to='escolas/')
    nome_curso = models.CharField(max_length=70)
    tipo_ensino = models.CharField(max_length=30)
    periodo = models.CharField(max_length=30)
    morada = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    linkdln = models.URLField()
    link_professor = models.URLField(blank=True)
    nome = models.CharField(max_length=20)
    link_aluno = models.URLField(blank=True)

    def __str__(self):
        if self.link_aluno == "":
             return "Professor " + self.nome
        else:
            return "Aluno " + self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=30)
    acronimo = models.CharField(max_length=5)
    ano = models.IntegerField()
    criador = models.CharField(max_length=30)
    logotipo = models.ImageField(upload_to='tecnologias/')
    link = models.URLField()
    descricao = models.CharField(max_length=100)
    BackEnd = models.BooleanField(default=False)
    FrontEnd = models.BooleanField(default=False)
    Outra = models.BooleanField(default=False)
    codigo = models.ImageField(upload_to="codigos/",blank=True)
    def __str__(self):
        return self.nome

class TrabalhoCurso(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    orientador = models.ManyToManyField(Pessoa,related_name='Orientador')
    ano = models.IntegerField()
    resumo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    github = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    relatorio = models.FileField(upload_to='trabalhos/')

    def __str__(self):
        return self.titulo

class Laboratorio(models.Model):
    link = models.URLField()
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='noticias/')
    link = models.URLField(default='')
    def __str__(self):
        return self.titulo

class Projeto(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='projetos/')
    ano = models.IntegerField()
    participantes = models.ManyToManyField(Pessoa)
    github = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia)
    def __str__(self):
        return self.titulo

class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    semestre = models.IntegerField(
            default=1,
            validators=[
                MaxValueValidator(2),
                MinValueValidator(1)
            ]
        )
    Etcs = models.IntegerField()
    topicos = models.CharField(max_length=1000)
    ranking = models.IntegerField(
            default=1,
            validators=[
                MaxValueValidator(5),
                MinValueValidator(1)
            ]
        )
    ano_letivo = models.CharField(max_length=10)
    link = models.URLField(blank=True)
    professor = models.ManyToManyField(Pessoa)
    projeto = models.ForeignKey(Projeto,on_delete=models.CASCADE,blank=True,null=True)
    imagem = models.ImageField(upload_to='cadeiras/',default='')
    def __str__(self):
        return self.nome

class Competencia (models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    cadeira = models.ManyToManyField(Cadeira, blank=True)
    projeto = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):
        return self.titulo

class Certificado(models.Model):
    nome = models.CharField(max_length=50)
    referencia = models.CharField(max_length=30)
    periodo = models.IntegerField()
    empresa = models.CharField(max_length=30)
    formador = models.URLField()
    ficheiro = models.FileField(upload_to='formadores/')

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='interesses/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

class Linguagem(models.Model):
    nome = models.CharField(max_length=20)
    certificado = models.URLField(blank=True)
    compreensao = models.CharField(max_length=2)
    conversacao= models.CharField(max_length=2)
    escrita = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=30)
    apelido = models.CharField(max_length=30)
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Comentarios(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome