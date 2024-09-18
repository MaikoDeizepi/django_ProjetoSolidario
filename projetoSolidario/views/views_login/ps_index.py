from django.shortcuts import render, redirect
from projetoSolidario.forms.usuario.form_user import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from projetoSolidario.forms.usuario.nao_usar import UsuarioForm


def index(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Logado com sucesso!")
            return redirect("projetosolidario:home")
        else:
            messages.error(request, "Login inválido")
    else:
        form = AuthenticationForm()

    return render(request, "projetoSolidario/tela_login/index.html", {"form": form})


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect("projetosolidario:index")

        context = {
            "form": form,
        }
        return render(
            request, "projetoSolidario/tela_login/criar_cadastro.html", context
        )

    context = {
        "form": RegisterForm(),
    }
    return render(request, "projetoSolidario/tela_login/criar_cadastro.html", context)


def login_view(request):
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Logado com sucesso!")
            return redirect("projetosolidario:home")
        messages.error(request, "Login inválido")

    return render(request, "projetoSolidario/tela_login/index.html", {"form": form})


@login_required(login_url="projetosolidario:index")
def logout_view(request):
    auth.logout(request)
    return redirect("projetosolidario:index")
