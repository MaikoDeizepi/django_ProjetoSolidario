from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def enviar_email_cadastro(form):

    # Renderiza o conteúdo HTML com os dados do usuário
    html_content = render_to_string(
        "projetoSolidario/tela_email/cadastro_empresa.html",
        {
            "nome_fantasia": form.nome_fantasia,
        },
    )
    text_content = strip_tags(html_content)  # Converte o HTML para texto simples

    # Cria o e-mail
    email = EmailMultiAlternatives(
        "Cadastro Confirmado - Bem-vindo ao Projeto Solidário",  # Assunto do e-mail
        text_content,  # Conteúdo em texto simples
        settings.EMAIL_HOST_USER,  # Remetente (usado no EMAIL_HOST_USER)
        [form.email],  # Destinatário (e-mail do usuário)
    )
    email.attach_alternative(html_content, "text/html")  # Anexa o conteúdo HTML
    email.send()  # Envia o e-mail
