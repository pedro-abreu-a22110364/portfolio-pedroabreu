from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from portfolio.models import *


# Create your views here.

def home_page_view(request):
    return render(request, 'portfolio/home.html')


def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentacao.html')


def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')


def formacao_page_view(request):
    return render(request, 'portfolio/formacao.html')


def projetos_page_view(request):
    projetos = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', projetos)


def tfc_page_view(request):
    tfcs = Tfc.objects.all()
    pessoas = Pessoa.objects.all()

    context = {
        'tfcs': tfcs,
        'pessoas': pessoas
    }

    return render(request, 'portfolio/tfc.html', context)


def contactos_page_view(request):
    contactos = {'contactos': Contacto.objects.all()}
    return render(request, 'portfolio/contacto.html', contactos)


def licenciatura_page_view(request):
    cadeiras = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', cadeiras)


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
