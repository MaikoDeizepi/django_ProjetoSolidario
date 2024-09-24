from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from projetoSolidario.forms.empresa.cadastro_empresa import EmpresaForm
from django.urls import reverse
from projetoSolidario.models import Empresa
from django.contrib.auth.decorators import login_required
from projetoSolidario.views.views_email.ps_email_cadastro_empresa import (
    enviar_email_cadastro,
)


@login_required(login_url="projetosolidario:index")
def empresa(request):

    contexto = {
        "title": "Empresa",
    }

    return render(request, "projetoSolidario/tela_empresa/empresa.html", contexto)


@login_required(login_url="projetosolidario:index")
def tela_cadastro(request):
    form_action = reverse("projetosolidario:telacadastro")

    if request.method == "POST":
        form = EmpresaForm(request.POST)

        context = {
            "form": form,
            "form_action": form_action,
            "title": "Cadastro Empresa",
        }

        if form.is_valid():
            empresa = form.save()
            enviar_email_cadastro(empresa)
            return redirect("projetosolidario:empresa")

        return render(
            request, "projetoSolidario/tela_empresa/tela_cadastro.html", context
        )

    context = {
        "form": EmpresaForm(),
        "form_action": form_action,
        "title": "Cadastro Empresa",
    }

    return render(request, "projetoSolidario/tela_empresa/tela_cadastro.html", context)


@login_required(login_url="projetosolidario:index")
def updateempresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    form_action = reverse("projetosolidario:updatempresa", args=(empresa_id,))

    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)

        context = {
            "form": form,
            "form_action": form_action,
            "title": "Cadastro Empresa",
        }

        if form.is_valid():
            empresa = form.save()
            return redirect("projetosolidario:editaridempresa", empresa_id)

        return render(
            request, "projetoSolidario/tela_empresa/tela_cadastro.html", context
        )

    context = {
        "form": EmpresaForm(instance=empresa),
        "form_action": form_action,
        "title": "Cadastro Empresa",
    }

    return render(request, "projetoSolidario/tela_empresa/tela_cadastro.html", context)


@login_required(login_url="projetosolidario:index")
def deletempresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)

    confirmation = request.POST.get("confirmation", "no")

    if confirmation == "yes":
        empresa.delete()
        return redirect("projetosolidario:editarempresa")

    return render(
        request,
        "projetoSolidario/tela_empresa/editar_id.html",
        {"empresa": empresa, "confirmation": confirmation},
    )
