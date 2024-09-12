from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.

class Evento(models.Model):
    EVENTO_CHOICES = (
        ("C", "Doação de Comida"),
        ("R", "Doação de Roupas"),
        ("P", "Doação de Pets+"),
        ("E", "Evento Assistencial"),
        ("O", "Outros"),
    )
    
    tipo_evento = models.CharField(max_length=1, choices=EVENTO_CHOICES, blank=False, null=False)
    nome_organizador = models.CharField(max_length=50)
    nome_evento = models.CharField(max_length= 100)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    data_evento = models.DateTimeField(default=timezone.now,)
    
    local_evento = models.CharField(max_length=50)
    limite_evento = models.CharField(max_length=5)
    
    
    def __str__(self):
        return f'{self.nome_organizador} {self.tipo_evento}'


    
    
class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100 )
    cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(max_length=254 )
    
    def __str__(self):
        return f'{self.razao_social} {self.nome_fantasia}'
    
class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.rua} {self.cidade} '

class Usuario(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("L", "LGBTQIA+"),
        ("P", "Prefiro Não Responder"),
        
    )
    
    primeiro_nome = models.CharField(max_length=50, blank=True)
    ultimo_nome = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    data_nascimento = models.DateField(blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    telefone = models.CharField(max_length=50, blank=True)
    senha = models.CharField(max_length=100,null=False, blank=True, )
    imagem_perfil = models.ImageField(blank=True, upload_to="pictures/%Y/%m/")
    #endereco = models.ForeignKey(
    #    Endereco, 
    #    on_delete=models.SET_NULL,
    #    blank=True, null=True
    # )
  
    
    def __str__(self):
        return f'{self.primeiro_nome} {self.ultimo_nome}'    
    

from django.db import models

class Calendario(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

    

    
    
    

    
    
    
    
    
