from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
def tela_evento(request):

    return render(
        request,
        "projetoSolidario/tela_evento/tela_evento.html",
    )
