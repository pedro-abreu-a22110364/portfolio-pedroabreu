from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('competencias', views.competencias_page_view, name='competencias'),
    path('formacao', views.formacao_page_view, name='formacao'),
    path('hobbies', views.hobbies_page_view, name='hobbies'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('tfc', views.tfc_page_view, name='tfc'),
    path('contacto', views.contactos_page_view, name='contactos'),
    path('blogCriar', views.blogCriar_page_view, name='blogCriar'),
    path('blogEditar/<int:blog_id>', views.blogEditar_page_view, name='blogEditar'),
    path('blogApagar/<int:blog_id>', views.blogApagar_page_view, name='blogApagar'),
    path('blog', views.blog_page_view, name='blog'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('video', views.video_page_view, name='video')
]
