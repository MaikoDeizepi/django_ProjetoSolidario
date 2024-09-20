from django.urls import path
from . import views

app_name = "projetosolidario"

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    # TELALOGIN
    path("projetosolidario/tela_login/forms", views.register, name="criaruser"),
    path("projetosolidario/", views.logout_view, name="logout"),
    # TELAHOME
    path("projetosolidario/home", views.home, name="home"),
    # TELACADASTROEMPRESA
    path(
        "projetosolidario/telacadastro_alterar/<int:empresa_id>/",
        views.editar_id_empresa,
        name="editaridempresa",
    ),
    path(
        "projetosolidario/telacadastro_alterar/<int:empresa_id>/update/",
        views.updateempresa,
        name="updatempresa",
    ),
    path(
        "projetosolidario/telacadastro_alterar/<int:empresa_id>/delete/",
        views.deletempresa,
        name="deletempresa",
    ),
    path("projetosolidario/empresa/", views.empresa, name="empresa"),
    path("projetosolidario/telacadastro/", views.tela_cadastro, name="telacadastro"),
    # aqui estou no ID unico para alterar
    path(
        "projetosolidario/telacadastro_alterar/",
        views.criar_cadastro,
        name="alterarcadastro",
    ),
    path(
        "projetosolidario/telacadastro_alterar/search/",
        views.search_empresa,
        name="searchempresa",
    ),
    path(
        "projetosolidario/telacadastro_consultar/",
        views.editar_empresa,
        name="editarempresa",
    ),
    # TELACADASTROEVENTOS
    path(
        "projetosolidario/telaevento_editar_evento/<int:evento_id>/",
        views.editar_id_evento,
        name="editaridevento",
    ),
    path(
        "projetosolidario/telaevento_editar_evento/<int:evento_id>/update/",
        views.updateevento,
        name="updateevento",
    ),
    path(
        "projetosolidario/telaevento_editar_evento/<int:evento_id>/delete/",
        views.deleteevento,
        name="deletevento",
    ),
    path("projetosolidario/eventos/", views.eventos, name="eventos"),
    path(
        "projetosolidario/telaevento_criar_evento/",
        views.criar_evento,
        name="criarevento",
    ),
    path(
        "projetosolidario/telaevento_consultar_evento/search/",
        views.search_evento,
        name="searchevento",
    ),
    path(
        "projetosolidario/telaevento_consultar_evento/",
        views.consultar_eventos,
        name="consultarevento",
    ),
    # TELASOBRENOS
    path("projetosolidario/sobrenos/", views.sobre_nos, name="sobrenos"),
    # TELAPERFIL
    path("projetosolidario/perfil/", views.tela_perfil, name="perfil"),
    # TELACALENDARIO
    path("projetosolidario/calendario/", views.CalendarView.as_view(), name="calendar"),
    # path("projetosolidario/evento/novo/", views.EventView.as_view(), name="event_new"),
    path(
        "projetosolidario/evento/edit/<int:event_id>/",
        views.EventView.as_view(),
        name="event_edit",
    ),
]
