from django.db import models

# Create your models here.

class Fruta(models.Model):
    choices = (
        ("Corte", "Corte"),
        ("Despolpar", "Despolpar"),
    )
    
    nome = models.CharField(max_length=100, unique = True)
    preco = models.FloatField()
    condicao = models.CharField(max_length= 20, choices=choices, null = True, blank = True)
    
    def __str__(self):
        return self.nome