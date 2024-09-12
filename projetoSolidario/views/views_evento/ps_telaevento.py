from django.shortcuts import render


def tela_evento(request):
  
    return render(
        request,
        'projetoSolidario/tela_evento/tela_evento.html',
      
        
    )