from ast import Str
from turtle import ondrag
from webbrowser import get
from django.db import models
from django.contrib.auth.models import User

class Kisealoadas(models.Model):
    class Meta():
        verbose_name = 'Kiselőadás'
        verbose_name_plural = 'Kiselőadások'

    tema = models.CharField('téma', max_length=255)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def setUser(betema, beuser):
        valtoztatott = Kisealoadas.objects.get(tema=betema)
        valtoztatott.user = beuser


    def __str__(self) -> str:
        return f"{self.tema}"
