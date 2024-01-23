from django.db import models
from apps.partners.models import Produtor
from django.core.exceptions import ValidationError

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
    
class EstoqueFruta(models.Model):
    quantidade_atual = models.IntegerField()
    quantidade_max = models.IntegerField(default = 50)
    
class Compra(models.Model):
    quantidade = models.FloatField()
    fruta = models.ForeignKey(Fruta, on_delete=models.CASCADE, null=True, blank=True)
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE, null=True, blank=True)
    create_ad = models.DateTimeField(auto_now_add = True)
    espaco_estoque = models.IntegerField()
    estoque = models.ForeignKey(EstoqueFruta, on_delete=models.CASCADE, null=True, blank=True)
    
class Producao(models.Model):
    quantidade_produzida = models.FloatField()
    fruta = models.ForeignKey(Fruta, on_delete=models.CASCADE, null=True, blank=True)
    data_producao = models.DateTimeField(auto_now_add = True)
    quantidade_reduzida = models.IntegerField()
    estoque = models.ForeignKey(EstoqueFruta, on_delete=models.CASCADE, null=True, blank=True)