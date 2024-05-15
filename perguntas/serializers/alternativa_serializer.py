from rest_framework import serializers
from ..models.alternativa import Alternativa

class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ['id', 'letra', 'texto','imagem', 'correta', 'pergunta_relacionada']
