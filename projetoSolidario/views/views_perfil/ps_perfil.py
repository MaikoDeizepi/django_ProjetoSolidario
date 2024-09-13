from django.shortcuts import render
from projetoSolidario.models import Usuario
from projetoSolidario.forms.usuario.form_user import RegisterForm

from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
def tela_perfil(request):

    # usuario = RegisterForm.cleaned_data.get('user.is_au')
    usuario = Usuario.objects.filter(pk="13")

    contexto = {
        "usuario": usuario,
    }

    return render(request, "projetoSolidario/tela_perfil/tela_perfil.html", contexto)
