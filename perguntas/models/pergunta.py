from django.db import models

class Pergunta(models.Model):
    texto = models.CharField(max_length=255)
    def __str__(self):
        return self.texto

