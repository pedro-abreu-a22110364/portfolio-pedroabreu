from datetime import datetime

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from portfolio.forms import *
from portfolio.models import *


# Create your views here.

def home_page_view(request):
    return render(request, 'portfolio/home.html')


def competencias_page_view(request):
    competencias = {'competencias': Competencia.objects.all()}
    return render(request, 'portfolio/competencias.html', competencias)


def formacao_page_view(request):
    formacoes = {'formacoes': Formacao.objects.all()}
    return render(request, 'portfolio/formacao.html', formacoes)


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


def hobbies_page_view(request):
    hobbies = {'hobbies': Hobbie.objects.all()}
    return render(request, 'portfolio/hobbies.html', hobbies)


def contactos_page_view(request):
    contactos = {'contactos': Contacto.objects.all()}
    return render(request, 'portfolio/contacto.html', contactos)


def licenciatura_page_view(request):
    cadeiras = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', cadeiras)


def blogCriar_page_view(request):
    form = ArtigoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/blogCriar.html', context)


def blog_page_view(request):
    artigos = {'artigos': Artigo.objects.all()}
    return render(request, 'portfolio/blog.html', artigos)


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


def logout_view(request):
    logout(request)
    return render(request, 'portfolio/login.html', {'message': "Logged Out"})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            artigos = {'artigos': Artigo.objects.all()}
            return render(request, 'portfolio/blog.html', artigos)
        else:
            return render(request, 'portfolio/login.html', {
                'menssage': "Invalid credentials"
            })
    return render(request, 'portfolio/login.html')


@login_required
def blogApagar_page_view(request, blog_id):
    Artigo.objects.get(id=blog_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


@login_required
def blogEditar_page_view(request, blog_id):
    blog = Artigo.objects.get(id=blog_id)
    form = ArtigoForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'blog_id': blog_id, }

    return render(request, 'portfolio/blogEditar.html', context)


def video_page_view(request):
    return render(request, 'portfolio/video.html')


def cidade_page_view(request):
    cidades = {'cidades': Cidade.objects.all()}
    return render(request, 'portfolio/cidade.html', cidades)
