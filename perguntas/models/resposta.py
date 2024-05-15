from django.db import models
from django.contrib.auth.models import User

class Resposta(models.Model):
    pergunta = models.ForeignKey('Pergunta', on_delete=models.CASCADE)
    alternativa = models.ForeignKey('Alternativa', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    horario_criacao = models.DateTimeField(auto_now_add=True)
    correta = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        # Verifica se a alternativa selecionada é a correta
        if self.alternativa.correta:
            self.correta = True
        else:
            self.correta = False
        
        super().save(*args, **kwargs)  # Chama o método save() original

    def __str__(self):
        return f'Resposta de {self.usuario.username} para a pergunta "{self.pergunta.texto}"'
