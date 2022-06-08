from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('home', views.home_view, name='home'),
    path('sobre', views.sobre_view, name='sobre'),
    path('projetos', views.projetos_view, name='projetos'),
    path('web', views.web_view, name='web'),
    path('blog', views.blog_view, name='blog'),
    path('contacto', views.contacto_view, name='contacto'),
    path('post_novo/', views.novo_post_view,name= 'post_novo'),
    path('post_edita/<int:post_id>', views.edita_post_view,name='post_edita'),
    path('post_apaga/<int:post_id>', views.apaga_post_view,name='post_apaga'),
    path('quizz', views.quizz, name='quizz'),
    path('projeto_novo/', views.novo_projeto_view, name='projeto_novo'),
    path('projeto_edita/<int:projeto_id>', views.edita_projeto_view,name='projeto_edita'),
    path('projeto_apaga/<int:projeto_id>', views.apaga_projeto_view,name='projeto_apaga'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),
    path('comentario_novo/', views.novo_comentario_view, name='comentario_novo'),
    path('comentario_edita/<int:comentario_id>', views.edita_comentario_view,name='comentario_edita'),
    path('comentario_apaga/<int:comentario_id>', views.apaga_comentario_view,name='comentario_apaga'),
    path('trabalho_novo/', views.novo_trabalho_view, name='trabalho_novo'),
    path('trabalho_edita/<int:trabalho_id>', views.edita_trabalho_view, name='trabalho_edita'),
    path('trabalho_apaga/<int:trabalho_id>', views.apaga_trabalho_view, name='trabalho_apaga'),
]