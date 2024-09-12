from django.shortcuts import render


def eventos(request):
  
    return render(
        request,
        'projetoSolidario/tela_evento/eventos.html',
      
        
    )