from django.shortcuts import render, redirect
from projetoSolidario.forms.endereco.cadastro_endereco import EnderecoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
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
            return redirect("projetosolidario:criarevento")

        return render(
            request, "projetoSolidario/tela_endereco/tela_endereco.html", context
        )

    context = {
        "form": EnderecoForm(),
        "form_action": form_action,
        "title": "Cadastro Endereco",
    }
    return render(request, "projetoSolidario/tela_endereco/tela_endereco.html", context)
