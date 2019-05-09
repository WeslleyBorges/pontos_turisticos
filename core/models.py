from django.db import models

# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    def Meta(self):
        verbose_name = 'Pontos Turisticos'

    def __str__(self):
        return self.nome