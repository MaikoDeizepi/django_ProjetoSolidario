from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def enviar_email_cadastro(form):

    # Renderiza o conteúdo HTML com os dados do usuário
    html_content = render_to_string(
        "projetoSolidario/tela_email/cadastro_evento.html",
        {
            "empresa": form.empresa,
            "rua": form.endereco.rua,
            "numero": form.endereco.numero,
            "bairro": form.endereco.bairro,
            "cidade": form.endereco.cidade,
            "estado": form.endereco.cidade,
            "pais": form.endereco.cidade,
            "tipo_evento": form.get_tipo_evento_display,
            "nome_organizador": form.nome_organizador,
            "nome_evento": form.nome_evento,
            "telefone": form.telefone,
            "email": form.email,
            "data_evento": form.data_evento,
            "limite_evento": form.limite_evento,
        },
    )
    text_content = strip_tags(html_content)  # Converte o HTML para texto simples

    # Cria o e-mail
    email = EmailMultiAlternatives(
        "Evento Criado - Bem-vindo ao Projeto Solidário",  # Assunto do e-mail
        text_content,  # Conteúdo em texto simples
        settings.EMAIL_HOST_USER,  # Remetente (usado no EMAIL_HOST_USER)
        [form.email],  # Destinatário (e-mail do usuário)
    )
    email.attach_alternative(html_content, "text/html")  # Anexa o conteúdo HTML
    email.send()  # Envia o e-mail


def enviar_email_cadastro_atualizar(form, valores_alterados):

    # Renderiza o conteúdo HTML com os dados do usuário
    html_content = render_to_string(
        "projetoSolidario/tela_email/cadastro_evento_atualizar.html",
        {
            "nome_organizador": form.nome_organizador,
            "valores_alterados": valores_alterados,
        },
    )
    text_content = strip_tags(html_content)  # Converte o HTML para texto simples

    # Cria o e-mail
    email = EmailMultiAlternatives(
        "Evento Alterado - Bem-vindo ao Projeto Solidário",  # Assunto do e-mail
        text_content,  # Conteúdo em texto simples
        settings.EMAIL_HOST_USER,  # Remetente (usado no EMAIL_HOST_USER)
        [form.email],  # Destinatário (e-mail do usuário)
    )
    email.attach_alternative(html_content, "text/html")  # Anexa o conteúdo HTML
    email.send()  # Envia o e-mail


def enviar_email_cadastro_exclusao(form):

    # Renderiza o conteúdo HTML com os dados do usuário
    html_content = render_to_string(
        "projetoSolidario/tela_email/cadastro_evento_excluir.html",
        {
            "nome_organizador": form.nome_organizador,
            "nome_evento": form.nome_evento,
        },
    )
    text_content = strip_tags(html_content)  # Converte o HTML para texto simples

    # Cria o e-mail
    email = EmailMultiAlternatives(
        "Evento Excluido -  Projeto Solidário",  # Assunto do e-mail
        text_content,  # Conteúdo em texto simples
        settings.EMAIL_HOST_USER,  # Remetente (usado no EMAIL_HOST_USER)
        [form.email],  # Destinatário (e-mail do usuário)
    )
    email.attach_alternative(html_content, "text/html")  # Anexa o conteúdo HTML
    email.send()  # Envia o e-mail
