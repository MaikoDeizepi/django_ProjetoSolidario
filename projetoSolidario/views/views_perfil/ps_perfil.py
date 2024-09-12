from django.shortcuts import render
from projetoSolidario.models import Usuario
from django.shortcuts import get_object_or_404


def tela_perfil(request):

    usuario = Usuario.objects.filter(pk="13")

    contexto = {
        "usuario": usuario,
    }

    return render(request, "projetoSolidario/tela_perfil/tela_perfil.html", contexto)
