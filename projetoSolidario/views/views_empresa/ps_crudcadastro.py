from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
def criar_cadastro(request):

    contexto = {
        "title": "Alterar Empresa",
    }

    return render(request, "projetoSolidario/tela_empresa/crud_cadastro.html", contexto)
