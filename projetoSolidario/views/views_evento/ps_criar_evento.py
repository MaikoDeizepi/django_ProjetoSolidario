from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from projetoSolidario.forms.evento.cadastro_evento import EventoForm
from projetoSolidario.models import Evento

#eventos


def criar_evento(request):
    form_action = reverse('projetosolidario:criarevento')


    if request.method == 'POST':
        form = EventoForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            return redirect('projetosolidario:eventos')



        return render(
            request,
            'projetoSolidario/tela_evento/criar_evento.html',
            context
        )

    context = {
        'form': EventoForm(),
        'form_action': form_action,
        'title': 'Cadastro Evento',
    }

    return render(
        request,
        'projetoSolidario/tela_evento/criar_evento.html',
        context
    )


def updateevento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    form_action = reverse('projetosolidario:updatevento', args=(evento_id,))
    
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)

        context = {
            'form': form,
            'form_action': form_action,
            'title': 'Editar Evento',  # Atualize o título para deixar claro que é edição
        }

        if form.is_valid():
            form.save()
            return redirect('projetosolidario:eventos')  # Redirecione para a lista de eventos

        # Se o form não for válido, renderize o mesmo template de edição
        return render(
            request,
            'projetoSolidario/tela_evento/editar_eventos.html',  # Verifique se o template está correto
            context
        )

    # Se for GET, exibe o formulário de edição
    context = {
        'form': EventoForm(instance=evento),
        'form_action': form_action,
        'title': 'Editar Evento',
    }
    return render(
        request,
        'projetoSolidario/tela_evento/editar_eventos.html',
        context
    )


def deleteevento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
       evento.delete()
       return redirect(
                    'projetosolidario:editaridevento'
                  )
    
    return render(
        request, 
        'projetoSolidario/tela_evento/editar_eventos.html',
        {
            'evento':evento,
            'confirmation':confirmation
        }
    )