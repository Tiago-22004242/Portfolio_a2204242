from django import forms
from .models import Post, Projeto, Comentarios, TrabalhoCurso, Escola, Cadeira, Tecnologia, Noticia, Competencia, \
    Certificado, Linguagem, Interesse


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'data': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Select a date','type': 'date'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Titulo'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL link'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Breve descricao'}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'autor': 'Autor',
            'data': 'Data',
            'titulo': 'Título',
            'link': 'Link',
            'descricao': 'Descrição',
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = '__all__'

class TrabalhoForm(forms.ModelForm):
    class Meta:
        model = TrabalhoCurso
        fields = '__all__'

class EscolaForm(forms.ModelForm):
    class Meta:
        model = Escola
        fields = '__all__'

class CadeiraForm(forms.ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'

class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = '__all__'

class LinguagemForm(forms.ModelForm):
    class Meta:
        model = Linguagem
        fields = '__all__'

class InteresseForm(forms.ModelForm):
    class Meta:
        model = Interesse
        fields = '__all__'