from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Avaliacao(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comentario = models.TextField()
    nota = models.DecimalField(decimal_places=2, max_digits=3)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' -> ' + str(self.data)
