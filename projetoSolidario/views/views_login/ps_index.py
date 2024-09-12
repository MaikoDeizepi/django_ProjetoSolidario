from django.shortcuts import render, redirect
from projetoSolidario.forms.usuario.cadastro_usuario import UsuarioForm
from django.urls import reverse


def index(request):
    return render(
        request,
        "projetoSolidario/tela_login/index.html",
    )


def criar_usuario(request):
    form_action = reverse("projetosolidario:criaruser")

    if request.method == "POST":
        # Inclui request.FILES para lidar com uploads de arquivos, como imagens de perfil
        form = UsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("projetosolidario:index")

        # Se o formulário não for válido, renderiza a página novamente com os erros
        context = {"form": form, "form_action": form_action}
        return render(
            request, "projetoSolidario/tela_login/criar_cadastro.html", context
        )

    # GET request: renderiza a página de criação de usuário com um formulário vazio
    context = {"form": UsuarioForm(), "form_action": form_action}

    return render(request, "projetoSolidario/tela_login/criar_cadastro.html", context)
