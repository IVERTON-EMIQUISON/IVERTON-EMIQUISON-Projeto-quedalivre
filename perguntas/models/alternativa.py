from django.db import models
from .pergunta import Pergunta


class Alternativa(models.Model):
    letra = models.CharField(max_length=5)
    texto = models.CharField(max_length=100)
    correta = models.BooleanField(default=False)
    pergunta_relacionada = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='perguntas/', null=True, blank=True)
    texto_adicional = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.texto
