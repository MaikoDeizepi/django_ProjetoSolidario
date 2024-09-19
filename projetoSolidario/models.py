from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Evento(models.Model):
    EVENTO_CHOICES = (
        ("C", "Doação de Comida"),
        ("R", "Doação de Roupas"),
        ("P", "Doação de Pets+"),
        ("E", "Evento Assistencial"),
        ("O", "Outros"),
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

    local_evento = models.CharField(max_length=50)
    limite_evento = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.nome_organizador} {self.tipo_evento}"


class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.razao_social} {self.nome_fantasia}"


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.rua} {self.cidade} "


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

    # endereco = models.ForeignKey(
    #    Endereco,
    #    on_delete=models.SET_NULL,
    #    blank=True, null=True
    # )


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
