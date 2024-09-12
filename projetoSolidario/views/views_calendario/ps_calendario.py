from django.shortcuts import render


def calendario(request):
    
    contexto = {
        
        'title': 'Calendario',
    }
  
    return render(
        request,
        'projetoSolidario/tela_calendario/tela_calendario.html',
        contexto
            
    )
