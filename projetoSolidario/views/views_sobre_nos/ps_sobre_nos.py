from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
def sobre_nos(request):

    return render(
        request,
        "projetoSolidario/tela_sobre_nos/sobre_nos.html",
    )
