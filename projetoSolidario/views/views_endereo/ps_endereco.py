from django.shortcuts import render, redirect, get_object_or_404
from projetoSolidario.forms.endereco.cadastro_endereco import EnderecoForm
from django.urls import reverse
from projetoSolidario.models import Endereco
from django.contrib.auth.decorators import login_required


def tela_cadastro_endereco(request):
    form_action = reverse("projetosolidario:criarendereco")

    if request.method == "POST":
        form = EnderecoForm(request.POST)

        context = {
            "form": form,
            "form_action": form_action,
            "title": "Cadastro Endereço",
        }

        if form.is_valid():
            form.save()
            return redirect("projetosolidario:criarendereco")

        return render(
            request, "projetoSolidario/tela_endereco/tela_endereco.html", context
        )

    context = {
        "form": EnderecoForm(),
        "form_action": form_action,
        "title": "Cadastro Endereco",
    }
    return render(request, "projetoSolidario/tela_endereco/tela_endereco.html", context)
