from django import forms
from .models import Post, Projeto, Comentarios, TrabalhoCurso


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