from rest_framework import viewsets
from ..models.alternativa import Alternativa
from ..serializers.alternativa_serializer import AlternativaSerializer

class AlternativaViewSet(viewsets.ModelViewSet):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer
