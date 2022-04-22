from ast import Str
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

class Kisealoadas(models.Model):
    class Meta():
        verbose_name = 'Kiselőadás'
        verbose_name_plural = 'Kiselőadások'

    tema = models.CharField('téma', max_length=255)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.tema}"
