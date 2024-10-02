from django.shortcuts import render, get_object_or_404, redirect
from projetoSolidario.models import Evento
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
def consultar_eventos(request):

    eventos = Evento.objects.filter(owner=request.user).order_by("id")

    paginator = Paginator(eventos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    contexto = {"page_obj": page_obj, "title": "Editar Eventos"}

    return render(request, "projetoSolidario/tela_evento/editar_eventos.html", contexto)


@login_required(login_url="projetosolidario:index")
def editar_id_evento(request, evento_id):

    single_contact = get_object_or_404(Evento.objects.filter(pk=evento_id))

    contexto = {"eventos": single_contact, "title": "Consultar Eventos"}

    return render(request, "projetoSolidario/tela_evento/editar_id.html", contexto)


@login_required(login_url="projetosolidario:index")
def search_evento(request):

    search_value = request.GET.get("q", "").strip()

    if search_value == "":
        return redirect("projetosolidario:consultarevento")

    eventos = Evento.objects.order_by("id").filter(
        Q(tipo_evento__icontains=search_value)
        | Q(nome_organizador__icontains=search_value)
        | Q(nome_evento__icontains=search_value)
        | Q(email__icontains=search_value)
        | Q(telefone__icontains=search_value)
        | Q(data_evento__icontains=search_value)
        | Q(local_evento__icontains=search_value)
        | Q(limite_evento__icontains=search_value)
    )

    print(eventos)

    paginator = Paginator(eventos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "search_value": search_value,
    }
    return render(request, "projetoSolidario/tela_evento/editar_eventos.html", context)
