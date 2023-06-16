from django.db import models


# Create your models here.


class Cadeira(models.Model):
    nome = models.CharField(max_length=50, default="Nome")
    ano = models.IntegerField(default=0)
    semestre = models.IntegerField(default=0)
    ects = models.IntegerField(default=0)
    topicos = models.CharField(max_length=500, default="Topicos", blank=True)
    ranking = models.IntegerField(default=0, blank=True)
    pagina = models.URLField(default="Sem link")

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, default="Nome")
    cargo = models.CharField(max_length=50, default="Sem cargo", blank=True)
    lusofona = models.URLField(default="Sem link", blank=True)
    linkedin = models.URLField(default="Sem link", blank=True)
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
    github = models.URLField(default="Sem link", blank=True)

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
    fotografia = models.ImageField(upload_to='tarefas/portfolio', null=True, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo


class Tfc(models.Model):
    titulo = models.CharField(max_length=100, default="Titulo")
    pessoas = models.ManyToManyField(Pessoa, blank=True)
    ano = models.IntegerField(default=0)
    resumo = models.CharField(max_length=500, default="Sumario")
    relatorio = models.URLField(default="Sem link")
    github = models.URLField(default="Sem link", blank=True)
    youtube = models.URLField(default="Sem link", blank=True)

    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    nome = models.CharField(max_length=50)
    link = models.URLField(max_length=300, default="Sem link", blank=True)
    fotografia = models.ImageField(upload_to='tarefas/portfolio', null=True, blank=True)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    curso = models.CharField(max_length=100)
    local = models.CharField(max_length=50)
    data_entrada = models.DateField (null=True, blank=True)
    data_saida = models.DateField(null=True, blank=True)
    logotipo = models.ImageField(upload_to='tarefas/portfolio', null=True, blank=True)

    def __str__(self):
        return self.curso


class Conta(models.Model):
    nome = models.CharField(max_length=100, default="Nome")
    github = models.URLField(default="Sem link")
    pythonanywhere = models.URLField(default="Sem link")

    def __str__(self):
        return self.nome


class Area(models.Model):
    nome = models.CharField(max_length=100, default="Nome")

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=100, default="Nome")
    areas_of_interest = models.ManyToManyField(Area)

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    data = models.DateField()
    autor = models.CharField(max_length=100, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True)
    titulo = models.CharField(max_length=100, default="Titulo")
    texto = models.TextField(max_length=1000, default="Texto")
    image = models.ImageField(upload_to='tarefas/portfolio', null=True, blank=True)
    link = models.URLField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comments')
    titulo = models.CharField(max_length=100, default="Titulo")
    texto = models.TextField(max_length=1000, default="Texto")

    def __str__(self):
        return self.titulo


class Cidade(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome
