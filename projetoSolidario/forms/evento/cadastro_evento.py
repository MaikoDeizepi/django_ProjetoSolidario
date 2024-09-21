import re
from django import forms
from django.core.exceptions import ValidationError
from projetoSolidario.models import Evento, Empresa, Endereco


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

    limite_evento = forms.IntegerField(
        widget=forms.NumberInput(attrs={"placeholder": "Digite o limite do seu evento"})
    )
    # Adicionar campo de escolha de empresa
    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),  # Certifique-se de que Empresa está importado corretamente
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
            "endereco",  # Incluindo campo empresa
        )

    def clean_telefone(self):
        telefone = self.cleaned_data.get("telefone")

        # Garantir que telefone seja uma string
        if not isinstance(telefone, str) or re.search(r"[a-zA-Z]", telefone):
            self.add_error(
                "telefone",
                ValidationError("O Telefone não deve conter letras", code="invalid"),
            )
        return telefone  # Retorna o telefone "limpo"
