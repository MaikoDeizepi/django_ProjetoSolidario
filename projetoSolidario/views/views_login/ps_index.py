from django.shortcuts import render, redirect
from projetoSolidario.forms.usuario.cadastro_usuario import UsuarioForm
from django.urls import reverse

def index(request):
    return render(
        request,
        'projetoSolidario/tela_login/index.html',
    )

def criar_usuario(request):
    form_action = reverse('projetosolidario:criaruser')

    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)  # Inclui request.FILES para lidar com uploads de arquivos

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save()
            return redirect('projetosolidario:index')

        return render(
            request,
            'projetoSolidario/tela_login/criar_cadastro.html',
            context
        )

    context = {
        'form': UsuarioForm(),
        'form_action': form_action
    }

    return render(
        request,
        'projetoSolidario/tela_login/criar_cadastro.html',
        context
    )
