from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    CEP = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField("Email", max_length=250, unique = True)
    CNPJ = models.CharField(max_length=100, unique = True)
    
    def __str__(self):
        return self.nome
    
class Produtor(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    CEP = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField("Email", max_length=250, unique = True)
    CPF = models.CharField(max_length=100, unique = True)
    
    def __str__(self):
        return self.nome