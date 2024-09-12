from django.shortcuts import render



def criar_cadastro(request):
    
    contexto = {
        
        'title': 'Alterar Empresa',
    }
  
    return render(
        request,
        'projetoSolidario/tela_empresa/crud_cadastro.html',
        contexto
        
            
    )