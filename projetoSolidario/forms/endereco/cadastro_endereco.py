import re
from django import forms
from django.core.exceptions import ValidationError
from projetoSolidario.models import Endereco


class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = (
            "rua",
            "numero",
            "bairro",
            "cidade",
            "estado",
            "pais",
        )
