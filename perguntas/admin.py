from django.contrib import admin
from .models.pergunta import Pergunta
from .models.alternativa import Alternativa
from .models.resposta import Resposta

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['id', 'texto']

@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
    list_display = ['id', 'letra', 'texto', 'correta', 'pergunta_relacionada']
    
@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ['id', 'pergunta', 'alternativa', 'usuario', 'horario_criacao', 'correta']
