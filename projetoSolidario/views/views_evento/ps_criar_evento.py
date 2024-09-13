from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from projetoSolidario.forms.evento.cadastro_evento import EventoForm
from projetoSolidario.models import Evento
from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
def criar_evento(request):
    form_action = reverse("projetosolidario:criarevento")

    if request.method == "POST":
        form_evento = EventoForm(request.POST)

        context = {
            "form_evento": form_evento,
            "form_action": form_action,
        }

        if form_evento.is_valid():
            form_evento.save()
            return redirect("projetosolidario:eventos")

        return render(
            request, "projetoSolidario/tela_evento/criar_evento.html", context
        )

    context = {
        "form_evento": EventoForm(),
        "form_action": form_action,
        "title": "Cadastro Evento",
    }

    return render(request, "projetoSolidario/tela_evento/criar_evento.html", context)


@login_required(login_url="projetosolidario:index")
def updateevento(request, evento_id):
    eventos = get_object_or_404(Evento, id=evento_id)
    form_action_evento = reverse("projetosolidario:updateevento", args=(evento_id,))

    if request.method == "POST":
        form_evento = EventoForm(request.POST, instance=eventos)

        context = {
            "form_evento": form_evento,
            "form_action_evento": form_action_evento,
            "title": "Cadastro Evento",
        }

        if form_evento.is_valid():
            form_evento.save()

            return redirect("projetosolidario:editaridevento", evento_id)

        return render(
            request, "projetoSolidario/tela_evento/criar_evento.html", context
        )

    context = {
        "form_evento": EventoForm(instance=eventos),
        "form_action_evento": form_action_evento,
        "title": "Cadastro Evento",
    }

    return render(request, "projetoSolidario/tela_evento/criar_evento.html", context)


@login_required(login_url="projetosolidario:index")
def deleteevento(request, evento_id):
    eventos = get_object_or_404(Evento, pk=evento_id)

    confirmation = request.POST.get("confirmation", "no")

    if confirmation == "yes":
        eventos.delete()
        return redirect("projetosolidario:consultarevento")

    return render(
        request,
        "projetoSolidario/tela_evento/editar_id.html",
        {"eventos": eventos, "confirmation": confirmation},
    )
