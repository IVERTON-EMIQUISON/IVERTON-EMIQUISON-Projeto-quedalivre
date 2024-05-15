from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewset.pergunta_viewset import PerguntaViewSet
from .viewset.alternativa_viewset import AlternativaViewSet
from .viewset.resposta_viewset import RespostaViewSet

# Criar um router padrão do Django REST Framework
router = DefaultRouter()

# Registrar o viewset PerguntaViewSet com o router
router.register(r'perguntas', PerguntaViewSet)
router.register(r'alternativas', AlternativaViewSet)
router.register(r'respostas', RespostaViewSet)

# Definir as URLs da sua aplicação
urlpatterns = [
    path('', include(router.urls)),  # Incluir as URLs do router
]
