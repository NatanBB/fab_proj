from django.db import models

# Create your models here.


class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    is_publicada = models.BooleanField(default=False)
