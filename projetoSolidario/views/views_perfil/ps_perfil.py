from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from projetoSolidario.models import Usuario


@login_required(login_url="projetosolidario:index")
def tela_perfil(
    request,
):

    # empresa = Empresa.objects.filter().all().order_by("id")
    usuario = request.user

    contexto = {
        "usuario": usuario,
    }

    return render(
        request, "projetoSolidario/tela_perfil/tela_perfil_teste.html", contexto
    )
