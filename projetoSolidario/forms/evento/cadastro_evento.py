import re
from django import forms
from django.core.exceptions import ValidationError
from projetoSolidario.models import Evento

class EventoForm(forms.ModelForm):
    
    nome_organizador = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu Nome'
            }
        )
    )
    nome_evento = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome do seu evento'
            }
        )
    )
    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu telefone'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(  # Alterei para EmailInput
            attrs={
                'placeholder': 'Digite seu email'
            }
        )
    )
    data_evento = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format='%d/%m/%Y %H:%M',  # Formato de data e hora
            attrs={
                'type': 'datetime-local',  # Tipo de entrada para data e hora
                'class': 'form-group',
                'placeholder': 'Selecione a data e hora do Evento'
            }
        )
    )
        
    local_evento = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o local do seu evento'
            }
        )
    )
    limite_evento = forms.IntegerField(  # Alterei para IntegerField
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Digite o limite do seu evento'
            }
        )
    )
    
    class Meta:
        model = Evento
        fields = (
            'nome_organizador', 'nome_evento', 'telefone', 'email',
            'data_evento', 'tipo_evento', 'local_evento', 'limite_evento',
        )
    
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        
        # Garantir que telefone seja uma string
        if not isinstance(telefone, str) or re.search(r'[a-zA-Z]', telefone):
            self.add_error(
                'telefone',
                ValidationError(
                    'O Telefone não deve conter letras',
                    code='invalid'
                )
            )
        return telefone  # Retorna o telefone "limpo"
