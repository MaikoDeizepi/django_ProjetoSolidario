from django.core.exceptions import ValidationError
import re
from django import forms
from django.contrib.auth.models import User
from projetoSolidario.models import Usuario


class UsuarioForm(forms.ModelForm):
    # Campos relacionados ao User
    primeiro_nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Digite seu Nome",
            }
        ),
        label="Primeiro Nome",
    )
    ultimo_nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Digite seu Sobrenome",
            }
        ),
        label="Último Nome",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Digite seu Email",
            }
        ),
        label="Email",
    )

    senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Digite sua Senha",
            }
        ),
        label="Senha",
    )

    class Meta:
        model = Usuario
        fields = ("data_nascimento", "sexo", "telefone", "imagem_perfil")

    def save(self, commit=True):
        usuario = super().save(commit=False)

        # Criando ou atualizando o User relacionado
        user = usuario.user
        user.first_name = self.cleaned_data["primeiro_nome"]
        user.last_name = self.cleaned_data["ultimo_nome"]
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]

        # Salvando a senha
        if self.cleaned_data["senha"]:
            user.set_password(self.cleaned_data["senha"])

        if commit:
            user.save()
            usuario.save()

        return usuario

    def clean_telefone(self):
        telefone = self.cleaned_data.get("telefone")

        # Garantir que telefone seja uma string e contenha apenas números
        if not isinstance(telefone, str) or not re.match(r"^\d+$", telefone):
            self.add_error(
                "telefone",
                ValidationError(
                    "O Telefone deve conter somente números", code="invalid"
                ),
            )
        return telefone

    # Função para validação de nome
    def clean(self):
        cleaned_data = super().clean()
        primeiro_nome = cleaned_data.get("primeiro_nome")  # Corrigido
        ultimo_nome = cleaned_data.get("ultimo_nome")  # Corrigido

        # Validação para garantir que o primeiro nome não seja igual ao último nome
        if primeiro_nome == ultimo_nome:
            self.add_error(
                "ultimo_nome",  # Corrigido
                ValidationError(
                    "O primeiro nome não pode ser igual ao sobrenome", code="invalid"
                ),
            )

        return cleaned_data

    # Função para validar o email
    def clean_email(self):
        email = self.cleaned_data.get("email")

        # Verificando se já existe um usuário com o mesmo e-mail no modelo User
        if User.objects.filter(email=email).exists():
            self.add_error(
                "email", ValidationError("Este e-mail já está em uso", code="invalid")
            )

        return email

    # Função para validar o usuário
    def clean_user(self):
        user = self.cleaned_data.get("user")

        # Verificando se o usuário já existe no modelo Usuario
        if Usuario.objects.filter(user=user).exists():
            self.add_error(
                "user", ValidationError("Este usuário já existe", code="invalid")
            )

        return user

    # Função para validar as senhas
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        # Verifica se as senhas são iguais
        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas não coincidem")

        return password2
