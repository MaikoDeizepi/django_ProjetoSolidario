from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from projetoSolidario.models import Usuario
import re


class RegisterForm(UserCreationForm):
    # Campos adicionais do modelo Usuario
    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            format="%d/%m/%Y",  # Formato de data e hora
            attrs={
                "type": "date",  # Tipo de entrada para data e hora
                "class": "form-group",
                "placeholder": "Selecione a data de nascimento",
            },
        )
    )

    sexo = forms.ChoiceField(
        choices=Usuario.SEXO_CHOICES,
        widget=forms.Select(attrs={"class": "classe-a classe-b"}),
        label="Sexo",
        required=True,
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Digite seu Telefone",
            }
        ),
        label="Telefone",
        required=False,
    )

    imagem_perfil = forms.ImageField(
        widget=forms.FileInput(attrs={"accept": "image/*"}),
        required=False,
        help_text="Adicione a sua imagem de perfil",
        label="Imagem de Perfil",
    )
    usable_password = None

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    # Função para validar o e-mail
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error(
                "email", ValidationError("Já existe este e-mail", code="invalid")
            )
        return email

    # Função para validar o telefone
    def clean_telefone(self):
        telefone = self.cleaned_data.get("telefone")
        if not isinstance(telefone, str) or not re.match(r"^\d+$", telefone):
            self.add_error(
                "telefone",
                ValidationError(
                    "O Telefone deve conter somente números", code="invalid"
                ),
            )
        return telefone

    # Função para salvar os dados de User e Usuario
    def save(self, commit=True):
        user = super().save(commit=False)  # Salva os dados do User
        if commit:
            user.save()

        # Agora, cria ou atualiza o objeto Usuario associado ao User
        usuario = Usuario(
            user=user,
            data_nascimento=self.cleaned_data.get("data_nascimento"),
            sexo=self.cleaned_data.get("sexo"),
            telefone=self.cleaned_data.get("telefone"),
            imagem_perfil=self.cleaned_data.get("imagem_perfil"),
        )

        if commit:
            usuario.save()

        return user
