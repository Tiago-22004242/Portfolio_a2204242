import matplotlib
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from matplotlib import pyplot as plt
import datetime
from .models import Post, Escola, Cadeira, Pessoa, Certificado, Competencia, Linguagem, PontuacaoQuizz, Projeto, \
    Tecnologia, TrabalhoCurso, Laboratorio, Noticia, Comentarios, Interesse
from .forms import PostForm, ProjetoForm, ComentarioForm, TrabalhoForm, EscolaForm, CadeiraForm, TecnologiaForm, \
    NoticiaForm, CompetenciaForm, CertificadoForm, LinguagemForm, InteresseForm
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
               'interesses': Interesse.objects.all(),
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
    return render(request, 'portfolio/web.html',context)


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

def novo_projeto_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = ProjetoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:projetos'))
    form = ProjetoForm()
    context = {'form': form}
    return render(request, 'portfolio/projeto_novo.html', context)

@login_required
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST,request.FILES,instance=projeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:projetos'))
    else:
        form = ProjetoForm(instance=projeto)
    context = {'form': form, 'projeto_id': projeto_id}
    return render(request, 'portfolio/projeto_edita.html', context)


def apaga_projeto_view(request, projeto_id):
    Projeto.objects.get(id=projeto_id).delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))

def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')

def view_logout(request):
    logout(request)
    return render(request, 'portfolio/login.html', {
        'message': 'Foi desconectado.'
    })

def novo_comentario_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = ComentarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:web'))
    form = ComentarioForm()
    context = {'form': form}
    return render(request, 'portfolio/comentario_novo.html', context)

@login_required
def edita_comentario_view(request, comentario_id):
    post = Comentarios.objects.get(id=comentario_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:web'))
    else:
        form = ComentarioForm(instance=post)
    context = {'form': form, 'comentario_id': comentario_id}
    return render(request, 'portfolio/comentario_edita.html', context)


def apaga_comentario_view(request, comentario_id):
    Comentarios.objects.get(id=comentario_id).delete()
    return HttpResponseRedirect(reverse('portfolio:web'))

def novo_trabalho_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = TrabalhoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:projetos'))
    form = TrabalhoForm()
    context = {'form': form}
    return render(request, 'portfolio/trabalho_novo.html', context)

@login_required
def edita_trabalho_view(request, trabalho_id):
    post = TrabalhoCurso.objects.get(id=trabalho_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:projetos'))
    else:
        form = TrabalhoForm(instance=post)
    context = {'form': form, 'trabalho_id': trabalho_id}
    return render(request, 'portfolio/trabalho_edita.html', context)


def apaga_trabalho_view(request, trabalho_id):
    TrabalhoCurso.objects.get(id=trabalho_id).delete()
    return HttpResponseRedirect(reverse('portfolio:web'))

def novo_escola_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = EscolaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    form = EscolaForm()
    context = {'form': form}
    return render(request, 'portfolio/escola_novo.html', context)

@login_required
def edita_escola_view(request, escola_id):
    post = Escola.objects.get(id=escola_id)
    if request.method == 'POST':
        form = EscolaForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    else:
        form = EscolaForm(instance=post)
    context = {'form': form, 'escola_id': escola_id}
    return render(request, 'portfolio/escola_edita.html', context)

def apaga_escola_view(request, escola_id):
    Escola.objects.get(id=escola_id).delete()
    return HttpResponseRedirect(reverse('portfolio:sobre'))

def novo_cadeira_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = CadeiraForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    form = CadeiraForm()
    context = {'form': form}
    return render(request, 'portfolio/cadeira_novo.html', context)

@login_required
def edita_cadeira_view(request, cadeira_id):
    post = Cadeira.objects.get(id=cadeira_id)
    if request.method == 'POST':
        form = CadeiraForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    else:
        form = CadeiraForm(instance=post)
    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'portfolio/cadeira_edita.html', context)

def apaga_cadeira_view(request, cadeira_id):
    Cadeira.objects.get(id=cadeira_id).delete()
    return HttpResponseRedirect(reverse('portfolio:sobre'))

def novo_tecnologia_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = TecnologiaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:web'))
    form = TecnologiaForm()
    context = {'form': form}
    return render(request, 'portfolio/tecnologia_novo.html', context)

@login_required
def edita_tecnologia_view(request, tecnologia_id):
    post = Tecnologia.objects.get(id=tecnologia_id)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:web'))
    else:
        form = TecnologiaForm(instance=post)
    context = {'form': form, 'tecnologia_id': tecnologia_id}
    return render(request, 'portfolio/tecnologia_edita.html', context)

def apaga_tecnologia_view(request, tecnologia_id):
    Tecnologia.objects.get(id=tecnologia_id).delete()
    return HttpResponseRedirect(reverse('portfolio:web'))

def novo_noticia_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = NoticiaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:web'))
    form = NoticiaForm()
    context = {'form': form}
    return render(request, 'portfolio/noticia_novo.html', context)

@login_required
def edita_noticia_view(request, noticia_id):
    post = Noticia.objects.get(id=noticia_id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:web'))
    else:
        form = NoticiaForm(instance=post)
    context = {'form': form, 'noticia_id': noticia_id}
    return render(request, 'portfolio/noticia_edita.html', context)

def apaga_noticia_view(request, noticia_id):
    Noticia.objects.get(id=noticia_id).delete()
    return HttpResponseRedirect(reverse('portfolio:web'))

def novo_competencia_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = CompetenciaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    form = CompetenciaForm()
    context = {'form': form}
    return render(request, 'portfolio/competencia_novo.html', context)

@login_required
def edita_competencia_view(request, competencia_id):
    post = Competencia.objects.get(id=competencia_id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    else:
        form = NoticiaForm(instance=post)
    context = {'form': form, 'competencia_id': competencia_id}
    return render(request, 'portfolio/competencia_edita.html', context)

def apaga_competencia_view(request, competencia_id):
    Competencia.objects.get(id=competencia_id).delete()
    return HttpResponseRedirect(reverse('portfolio:sobre'))

def novo_certificado_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = CertificadoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    form = CertificadoForm()
    context = {'form': form}
    return render(request, 'portfolio/certificado_novo.html', context)

@login_required
def edita_certificado_view(request, certificado_id):
    post = Certificado.objects.get(id=certificado_id)
    if request.method == 'POST':
        form = CertificadoForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    else:
        form = CertificadoForm(instance=post)
    context = {'form': form, 'certificado_id': certificado_id}
    return render(request, 'portfolio/certificado_edita.html', context)

def apaga_certificado_view(request, certificado_id):
    Certificado.objects.get(id=certificado_id).delete()
    return HttpResponseRedirect(reverse('portfolio:sobre'))

def novo_linguagem_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = LinguagemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    form = LinguagemForm()
    context = {'form': form}
    return render(request, 'portfolio/linguagem_novo.html', context)

@login_required
def edita_linguagem_view(request, linguagem_id):
    post = Linguagem.objects.get(id=linguagem_id)
    if request.method == 'POST':
        form = LinguagemForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    else:
        form = LinguagemForm(instance=post)
    context = {'form': form, 'linguagem_id': linguagem_id}
    return render(request, 'portfolio/linguagem_edita.html', context)

def apaga_linguagem_view(request, linguagem_id):
    Linguagem.objects.get(id=linguagem_id).delete()
    return HttpResponseRedirect(reverse('portfolio:sobre'))

def novo_interesse_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    if request.method == 'POST':
        form = InteresseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    form = InteresseForm()
    context = {'form': form}
    return render(request, 'portfolio/interesse_novo.html', context)

@login_required
def edita_interesse_view(request, interesse_id):
    post = Interesse.objects.get(id=interesse_id)
    if request.method == 'POST':
        form = InteresseForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:sobre'))
    else:
        form = InteresseForm(instance=post)
    context = {'form': form, 'interesse_id': interesse_id}
    return render(request, 'portfolio/interesse_edita.html', context)

def apaga_interesse_view(request, interesse_id):
    Interesse.objects.get(id=interesse_id).delete()
    return HttpResponseRedirect(reverse('portfolio:sobre'))