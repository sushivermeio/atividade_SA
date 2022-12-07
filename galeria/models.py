from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class RegistroLogin(Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    horario_entrada = models.DateTimeField()
    horario_saida = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username
