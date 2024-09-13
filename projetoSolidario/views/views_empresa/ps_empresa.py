from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
def empresa(request):

    contexto = {
        "title": "Empresa",
    }

    return render(request, "projetoSolidario/tela_empresa/empresa.html", contexto)
