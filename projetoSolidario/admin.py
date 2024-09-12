from django.contrib import admin
from projetoSolidario import models


# Register your models here.

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = 'id', 'primeiro_nome', 'ultimo_nome'

@admin.register(models.Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = 'id', 'razao_social', 'nome_fantasia'

@admin.register(models.Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = 'id', 'rua', 'cidade'
    
@admin.register(models.Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome_organizador', 'tipo_evento'

@admin.register(models.Calendario)
class CalendarioAdmin(admin.ModelAdmin):
    ...