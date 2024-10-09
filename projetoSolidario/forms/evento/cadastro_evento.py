import re
from django import forms
from django.core.exceptions import ValidationError
from projetoSolidario.models import Evento, Empresa, Endereco
from django.utils import timezone


class EventoForm(forms.ModelForm):
    nome_organizador = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Digite seu Nome"})
    )
    nome_evento = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Digite o nome do seu evento"})
    )
    telefone = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Digite seu telefone"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Digite seu email"})
    )
    data_evento = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format="%d/%m/%Y %H:%M",
            attrs={
                "type": "datetime-local",
                "class": "form-group",
                "placeholder": "Selecione a data e hora do Evento",
            },
        )
    )

    limite_evento = forms.CharField(
        widget=forms.NumberInput(attrs={"placeholder": "Digite o limite do seu evento"})
    )
    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Empresa que irá auxiliar no Evento",
    )

    endereco = forms.ModelChoiceField(
        queryset=Endereco.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Endereço do Evento",
    )

    class Meta:
        model = Evento
        fields = (
            "nome_organizador",
            "nome_evento",
            "telefone",
            "email",
            "data_evento",
            "tipo_evento",
            "limite_evento",
            "empresa",
            "endereco",
        )

    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["data_evento"].initial = self.instance.data_evento
        else:
            self.fields["data_evento"].initial = timezone.now()

    def clean_telefone(self):
        telefone = self.cleaned_data.get("telefone")

        # Garantir que telefone seja uma string
        if not isinstance(telefone, str) or re.search(r"[a-zA-Z]", telefone):
            self.add_error(
                "telefone",
                ValidationError("O Telefone não deve conter letras", code="invalid"),
            )
        return telefone  # Retorna o telefone "limpo"

    def clean_data_evento(self):
        data_evento = self.cleaned_data.get("data_evento")

        # Verificar se já existe algum evento na mesma data e horário
        eventos_conflitantes = Evento.objects.filter(data_evento=data_evento)

        # Excluir o próprio evento se for uma edição
        if self.instance and self.instance.pk:
            eventos_conflitantes = eventos_conflitantes.exclude(pk=self.instance.pk)

        if eventos_conflitantes.exists():
            raise ValidationError(
                "Já existe um evento marcado para esta data e horário.",
                code="data_conflito",
            )

        return data_evento

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        evento = super().save(commit=False)

        if commit:
            evento.save()

        return evento
