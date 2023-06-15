from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


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
    return render(request, 'portfolio/projetos.html')


def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


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