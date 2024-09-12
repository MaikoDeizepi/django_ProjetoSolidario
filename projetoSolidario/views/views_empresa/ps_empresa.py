from django.shortcuts import render


def empresa(request):
    
    contexto = {
        
        'title': 'Empresa',
    }
  
    return render(
        request,
        'projetoSolidario/tela_empresa/empresa.html',
        contexto
            
    )