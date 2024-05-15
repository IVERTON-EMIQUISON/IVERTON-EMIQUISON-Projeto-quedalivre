from rest_framework import serializers
from ..models.pergunta import Pergunta

class PerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = ['id', 'texto']
