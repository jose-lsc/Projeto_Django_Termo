from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
import random


class Palavra(models.Model):
    conteudo = models.CharField(max_length= 5, null=False, blank = False)


    def __str__(self) -> str:
        return self.conteudo
    
class PalavraDia(models.Model):

    dia = models.DateTimeField(
        
    )

    palavra = models.ForeignKey(
        Palavra,
        on_delete=models.CASCADE,
    )

class Usuario(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )
    tentativas = models.DecimalField(
        max_digits=1,
        decimal_places=0,
        validators=[MinValueValidator(0), MaxValueValidator(6)],
        default=0,
    )
    vidas = models.DecimalField(
        max_digits=1,
        decimal_places=0,
        default=6,
        validators=[MinValueValidator(0), MaxValueValidator(6)]
    )
    pontuacao = models.DecimalField(
        max_digits=9,
        decimal_places=0,
        default=0,
    )

class informacoes(models.Model):
    #palavra = banco_palavras.objects.values_list('conteudo', flat=True)
    #conjuntoDeLetras = list(palavra)
    pass
    
    
   
    
    