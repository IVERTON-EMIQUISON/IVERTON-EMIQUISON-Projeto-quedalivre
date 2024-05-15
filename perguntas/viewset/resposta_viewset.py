from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.alternativa import Alternativa
from ..models.pergunta import Pergunta
from ..models.resposta import Resposta
from ..serializers.resposta_serializer import RespostaSerializer


class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer

    @action(detail=False, methods=['post'])
    def criar_resposta(self, request):
        user_id = 1
        user = User.objects.get(pk=user_id)
        respostas = request.data
        for resposta in respostas:
            pergunta_id = resposta.get('pergunta_id')
            alternativa_id = resposta.get('alternativa_id')

            try:
                pergunta = Pergunta.objects.get(id=pergunta_id)
                alternativa = Alternativa.objects.get(id=alternativa_id, pergunta_relacionada=pergunta)
            except (Pergunta.DoesNotExist, Alternativa.DoesNotExist):
                return Response({'message': 'Pergunta ou alternativa não encontrada'}, status=404)

            Resposta.objects.create(
                pergunta=pergunta, alternativa=alternativa, usuario=user
            )

        return Response({'message': 'Respostas criadas com sucesso'}, status=201)
