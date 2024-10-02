from django.shortcuts import render, get_object_or_404, redirect
from projetoSolidario.models import Empresa
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
def editar_empresa(request):

    empresa = Empresa.objects.filter(owner=request.user).order_by("id")

    paginator = Paginator(empresa, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    contexto = {"page_obj": page_obj, "title": "Editar Empresas"}

    return render(
        request, "projetoSolidario/tela_empresa/editar_empresa.html", contexto
    )


@login_required(login_url="projetosolidario:index")
def editar_id_empresa(request, empresa_id):

    single_contact = get_object_or_404(Empresa.objects.filter(pk=empresa_id))

    contexto = {"empresa": single_contact, "title": "Editar Empresas"}

    return render(request, "projetoSolidario/tela_empresa/editar_id.html", contexto)


@login_required(login_url="projetosolidario:index")
def search_empresa(request):

    search_value = request.GET.get("q", "").strip()

    if search_value == "":
        redirect("projetosolidario:alterarcadastro")

    empresa = Empresa.objects.order_by("id").filter(
        Q(razao_social__icontains=search_value)
        | Q(nome_fantasia__icontains=search_value)
        | Q(cnpj__icontains=search_value)
        | Q(telefone__icontains=search_value)
        | Q(email__icontains=search_value)
    )
    paginator = Paginator(empresa, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    contexto = {"page_obj": page_obj, "search_value": search_value}

    return render(
        request, "projetoSolidario/tela_empresa/editar_empresa.html", contexto
    )
