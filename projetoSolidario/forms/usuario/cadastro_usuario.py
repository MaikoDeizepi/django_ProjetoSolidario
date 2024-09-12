import re
from django import forms
from django.core.exceptions import ValidationError
from projetoSolidario.models import Usuario

class UsuarioForm(forms.ModelForm):
    imagem_perfil = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )
    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',  # Isso faz com que o campo seja exibido como um seletor de data
                'class': 'form-group',  # Adiciona classes CSS para estilização, se necessário
                'placeholder': 'Selecione a data de nascimento'  # Placeholder opcional
            }
        )
    )
    primeiro_nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Digite seu Nome',
            }
        ),
        label='Primeiro Nome',
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Digite sua Senha',
            }
        ),
        label='Senha',
    )

    class Meta:
        model = Usuario
        fields = (
            'primeiro_nome', 'ultimo_nome', 'email',
            'data_nascimento', 'sexo', 'telefone', 'senha', 'imagem_perfil',
        )

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        
        # Garantir que telefone seja uma string
        if not isinstance(telefone, str) or not re.match(r'^\d+$', telefone):
            self.add_error(
                'telefone',
                ValidationError(
                    'O Telefone deve ter somente números',
                    code='invalid'
                )
            )
        return telefone

    def clean(self):
        cleaned_data = super().clean()
        primeiro_nome = cleaned_data.get('primeiro_nome')
        ultimo_nome = cleaned_data.get('ultimo_nome')

        # Validação para garantir que o primeiro nome não seja igual ao último nome
        if primeiro_nome == ultimo_nome:
            self.add_error(
                'ultimo_nome',
                ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid'
                )
            )

        return cleaned_data
