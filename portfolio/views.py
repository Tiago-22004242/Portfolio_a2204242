import matplotlib
from django.http import HttpResponseRedirect
from matplotlib import pyplot as plt
matplotlib.use("Qt5Agg")
import datetime
from .models import Post, Escola, Cadeira, Pessoa, Certificado, Competencia, Linguagem, PontuacaoQuizz, Projeto, \
    Tecnologia, TrabalhoCurso, Laboratorio, Noticia, Comentarios
from .forms import PostForm
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def home_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']
    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }
    return render(request, 'portfolio/home.html', context)


def sobre_view(request):
    context = {'escolas': Escola.objects.all(),
               'cadeiras': Cadeira.objects.all(),
               'pessoas': Pessoa.objects.all(),
               'certificados':  Certificado.objects.all(),
               'competencias': Competencia.objects.all(),
               'linguagens': Linguagem.objects.all(),
               }
    return render(request, 'portfolio/sobre.html', context)

def projetos_view(request):
    context = {'projetos': Projeto.objects.all(),
               'trabalhos': TrabalhoCurso.objects.all(),
               'competencias': Competencia.objects.all(),
               }
    return render(request, 'portfolio/projetos.html',context)

def web_view(request):
    context = { 'tecnologias': Tecnologia.objects.all(),
                'labs': Laboratorio.objects.all(),
                'noticias': Noticia.objects.all(),
                'comentarios': Comentarios.objects.all(),
    }
    return render(request, 'portfolio/web.html')


def contacto_view(request):
    return render(request, 'portfolio/contactos.html')


def blog_view(request):
    context = {'posts': Post.objects.all(),}
    return render(request, 'portfolio/blog.html', context)


def novo_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:blog'))
    form = PostForm()
    context = {'form': form}
    return render(request, 'portfolio/blog_novo.html', context)


def edita_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:blog'))
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/blog_edita.html', context)


def apaga_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def pontuacao_quiz(request):
    count = 0
    nome = request.POST['nome']
    apelido = request.POST['apelido']
    css = request.POST['CSS']
    margin = request.POST['leftMargin']
    simbolo = request.POST.get('symbol')
    if css == "css" or "CSS":
        count += 10
    if margin == "margin-left":
        count += 10
    if simbolo == "#":
        count+=10
    pyhton = request.POST.get('Pyhton')
    django = request.POST.get('Django')
    css = request.POST.get('CSS')
    if pyhton == "Pyhton":
        count += 10
    if django == "Django":
        count += 10
    if css == "CSS":
        count += 10
    data1 = datetime.date(2015,7,21)
    data2 = request.POST['dateFund']
    if data1 == data2:
        count += 10
    bytes = request.POST['bytes']
    if bytes == 8:
        count+= 10
    javascript = request.POST.get('Javascript')
    java = request.POST.get('Java')
    c = request.POST.get('C#')
    if javascript == "Javascript":
        count += 10
    return count

def desenha_grafico_resultados():
    participantes = sorted(PontuacaoQuizz.objects.all(), key=lambda t: t.pontuacao, reverse=True)
    nomes = []
    pontuacoes = []
    for pt in participantes:
        nomes.append(pt.nome + " "+pt.apelido)
        pontuacoes.append(pt.pontuacao)
    plt.barh(nomes, pontuacoes)
    plt.savefig("portfolio/static/portfolio/images/grafico.png", bbox_inches='tight')

def quizz(request):
    if request.method == 'POST':
        n = request.POST['nome']
        a = request.POST['apelido']
        p = pontuacao_quiz(request)
        r = PontuacaoQuizz(nome=n, apelido=a, pontuacao=p)
        r.save()
    desenha_grafico_resultados()
    return render(request,'portfolio/web.html')
