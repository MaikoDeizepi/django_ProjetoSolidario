from django.shortcuts import redirect
from django.contrib.auth import logout


class LogoutOnHomepageMiddleware:
    """
    Middleware que força o logout quando o usuário tenta acessar a página inicial.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Se o usuário está logado e tenta acessar a página inicial
        if request.user.is_authenticated and request.path == "/":
            logout(request)  # Faz logout
            return redirect("/")  # Redireciona para a página inicial deslogado

        # Continua com a execução normal
        response = self.get_response(request)
        return response
