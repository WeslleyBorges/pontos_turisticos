from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.username + ' -> ' + str(self.data)