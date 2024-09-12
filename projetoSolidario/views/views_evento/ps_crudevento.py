from django.shortcuts import render


def crud_evento(request):
  
    return render(
        request,
        'projetoSolidario/tela_evento/crud_evento.html',
            
    )