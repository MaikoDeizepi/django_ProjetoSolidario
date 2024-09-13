from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
def calendario(request):

    contexto = {
        "title": "Calendario",
    }

    return render(
        request, "projetoSolidario/tela_calendario/tela_calendario.html", contexto
    )
