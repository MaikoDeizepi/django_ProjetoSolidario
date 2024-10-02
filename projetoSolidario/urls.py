from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views.view_reset.ps_reset import *


app_name = "projetosolidario"

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    # TELALOGIN
    path("tela_login/forms/", views.register, name="criaruser"),
    path("projetosolidario/", views.logout_view, name="logout"),
    # TELAHOME
    path("home/", views.home, name="home"),
    # TELACADASTROEMPRESA
    path(
        "telacadastro_alterar/<int:empresa_id>/",
        views.editar_id_empresa,
        name="editaridempresa",
    ),
    path(
        "telacadastro_alterar/<int:empresa_id>/update/",
        views.updateempresa,
        name="updatempresa",
    ),
    path(
        "telacadastro_alterar/<int:empresa_id>/delete/",
        views.deletempresa,
        name="deletempresa",
    ),
    path("empresa/", views.empresa, name="empresa"),
    path("telacadastro/", views.tela_cadastro, name="telacadastro"),
    # aqui estou no ID unico para alterar
    path(
        "telacadastro_alterar/",
        views.criar_cadastro,
        name="alterarcadastro",
    ),
    path(
        "telacadastro_alterar/search/",
        views.search_empresa,
        name="searchempresa",
    ),
    path(
        "telacadastro_consultar/",
        views.editar_empresa,
        name="editarempresa",
    ),
    # TELACADASTROEVENTOS
    path(
        "telaevento_editar_evento/<int:evento_id>/",
        views.editar_id_evento,
        name="editaridevento",
    ),
    path(
        "telaevento_editar_evento/<int:evento_id>/update/",
        views.updateevento,
        name="updateevento",
    ),
    path(
        "telaevento_editar_evento/<int:evento_id>/delete/",
        views.deleteevento,
        name="deletevento",
    ),
    path("eventos/", views.eventos, name="eventos"),
    path(
        "telaevento_criar_evento/",
        views.criar_evento,
        name="criarevento",
    ),
    path(
        "telaevento_consultar_evento/search/",
        views.search_evento,
        name="searchevento",
    ),
    path(
        "telaevento_consultar_evento/",
        views.consultar_eventos,
        name="consultarevento",
    ),
    # TELASOBRENOS
    path("sobrenos/", views.sobre_nos, name="sobrenos"),
    # TELAPERFIL
    path("perfil/", views.tela_perfil, name="perfil"),
    # TELACALENDARIO
    path(
        "calendario/",
        login_required(views.CalendarView.as_view()),
        name="calendar",
    ),
    path("evento/editar/<int:pk>/", views.editar_evento, name="editar_evento"),
    # TELAENDERECO
    path("endereco/", views.tela_cadastro_endereco, name="criarendereco"),
    path(
        "password_reset/",
        CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset_done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
