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
    path('post_novo/', views.novo_post_view,name = 'post_novo'),
    path('post_edita/<int:post_id>', views.edita_post_view,name='post_edita'),
    path('post_apaga/<int:post_id>', views.apaga_post_view,name='post_apaga'),
    path('quizz', views.quizz, name='quizz')
]