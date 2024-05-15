from rest_framework import serializers
from ..models.resposta import Resposta

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = ['id', 'pergunta', 'alternativa', 'usuario', 'horario_criacao', 'correta']
