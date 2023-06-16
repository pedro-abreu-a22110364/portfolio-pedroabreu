from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('apresentacao', views.apresentacao_page_view, name='apresentacao'),
    path('competencias', views.competencias_page_view, name='competencias'),
    path('formacao', views.formacao_page_view, name='formacao'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('tfc', views.tfc_page_view, name='tfc')
]
