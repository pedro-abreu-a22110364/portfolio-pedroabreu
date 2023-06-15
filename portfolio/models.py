from django.db import models


# Create your models here.


class Cadeira(models.Model):
    nome = models.CharField(max_length=50, default="Nome")
    ano = models.IntegerField(default=0)
    semestre = models.IntegerField(default=0)
    ects = models.IntegerField(default=0)
    topicos = models.CharField(max_length=500, default="Topicos", blank=True)
    ranking = models.IntegerField(default=0, blank=True)
    pagina = models.CharField(max_length=300, default="Sem link")

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, default="Nome")
    cargo = models.CharField(max_length=50, default="Sem cargo", blank=True)
    lusofona = models.CharField(max_length=300, default="Sem link", blank=True)
    linkedin = models.CharField(max_length=300, default="Sem link", blank=True)
    cadeira = models.ManyToManyField(Cadeira, blank=True)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=100, default="Titulo")
    descricao = models.CharField(max_length=500, default="Descrição")
    imagem = models.ImageField(blank=True)
    ano = models.IntegerField(default=0)
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE, blank=True)
    participantes = models.ManyToManyField(Pessoa, blank=True)
    github = models.CharField(max_length=300, default="Sem link", blank=True)

    def __str__(self):
        return self.titulo


class Competencia(models.Model):
    titulo = models.CharField(max_length=100, default="Titulo")
    descricao = models.CharField(max_length=300, default="Descrição", blank=True)
    projetos = models.ManyToManyField(Projeto, blank=True)
    cadeiras = models.ManyToManyField(Cadeira, blank=True)

    def __str__(self):
        return self.titulo


class Hobbie(models.Model):
    titulo = models.CharField(max_length=100, default="Titulo")
    descricao = models.CharField(max_length=500, default="Descrição")
    fotografia = models.ImageField(blank=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.titulo


class Tfc(models.Model):
    titulo = models.CharField(max_length=100, default="Titulo")
    pessoas = models.ManyToManyField(Pessoa, blank=True)
    ano = models.IntegerField(default=0)
    resumo = models.CharField(max_length=500, default="Sumario")
    relatorio = models.CharField(max_length=300, default="Sem link")
    github = models.CharField(max_length=300, default="Sem link", blank=True)

    def __str__(self):
        return self.titulo


class Post(models.Model):
    titulo = models.CharField(max_length=100, default="Titulo")
    descricao = models.CharField(max_length=500, default="Descrição")
    autor = models.OneToOneField(Pessoa, on_delete=models.CASCADE, blank=True)
    data = models.DateField
    link = models.CharField(max_length=300, blank=True)
    fotografia = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo
