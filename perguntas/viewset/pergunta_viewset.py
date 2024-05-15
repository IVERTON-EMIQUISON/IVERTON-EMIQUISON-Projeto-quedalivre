from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.alternativa import Alternativa
from ..models.pergunta import Pergunta
from ..serializers.alternativa_serializer import AlternativaSerializer
from ..serializers.pergunta_serializer import PerguntaSerializer


class PerguntaViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

    @action(detail=False)
    def perguntas_com_alternativas(self, request):
        perguntas = self.get_queryset()
        data = []

        for pergunta in perguntas:
            pergunta_data = {
                'id': pergunta.id,
                'texto': pergunta.texto,
                'alternativas': []
            }
            alternativas = Alternativa.objects.filter(pergunta_relacionada=pergunta)
            for alternativa in alternativas:
                alternativa_data = {
                    'id': alternativa.id,
                    'letra': alternativa.letra,
                    'texto': alternativa.texto,
                    'correta': alternativa.correta
                }
                pergunta_data['alternativas'].append(alternativa_data)
            data.append(pergunta_data)

        return Response(data)
