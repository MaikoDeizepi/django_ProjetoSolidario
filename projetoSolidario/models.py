from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import pycountry

# Create your models here.


class Pais(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(
        Pais, on_delete=models.CASCADE
    )  # Adicione esta linha para a relação com País

    def __str__(self):
        return f"{self.nome} ({self.sigla})"


class Endereco(models.Model):
    estado = (
        ("C", "Doação de Comida"),
        ("R", "Doação de Roupas"),
        ("P", "Doação de Pets+"),
        ("E", "Evento Assistencial"),
        ("O", "Outros"),
    )
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.rua} {self.cidade} "


class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.razao_social} {self.nome_fantasia}"


class Evento(models.Model):
    EVENTO_CHOICES = (
        ("C", "Doação de Comida"),
        ("R", "Doação de Roupas"),
        ("P", "Doação de Pets+"),
        ("E", "Evento Assistencial"),
        ("O", "Outros"),
    )
    empresa = models.ForeignKey(
        Empresa, on_delete=models.SET_NULL, null=True, blank=True
    )
    endereco = models.ForeignKey(
        Endereco, on_delete=models.SET_NULL, null=True, blank=True
    )

    tipo_evento = models.CharField(
        max_length=1, choices=EVENTO_CHOICES, blank=False, null=False
    )
    nome_organizador = models.CharField(max_length=50)
    nome_evento = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    data_evento = models.DateTimeField(
        default=timezone.now,
    )
    limite_evento = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.nome_organizador} {self.tipo_evento}"

    def get_absolute_url(self):
        return reverse("projetosolidario:editar_evento", kwargs={"pk": self.pk})


class Usuario(models.Model):
    SEXO_CHOICES = (
        (" ", " "),
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("L", "LGBTQIA+"),
        ("P", "Prefiro Não Responder"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    data_nascimento = models.DateField(blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    telefone = models.CharField(max_length=20, blank=True)
    imagem_perfil = models.ImageField(blank=True, upload_to="pictures/%Y/%m/")


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Certificar-se de que `start_time` e `end_time` são timezone-aware
        if timezone.is_naive(self.start_time):
            self.start_time = timezone.make_aware(self.start_time)
        if timezone.is_naive(self.end_time):
            self.end_time = timezone.make_aware(self.end_time)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("projetosolidario:event_edit", kwargs={"event_id": self.pk})

    def __str__(self):
        return self.title
