from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    choices = (
        ("gerente", "gerente"),
        ("entregador", "entregador"),
        ("tec. alimentos", "tec. alimentos"),
        ("ger. de producao", "ger. de producao"),
        ("aux. de producao", "aux. de producao"),
    )
    
    username = models.CharField(max_length=150, unique=True)
    test = None
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    CEP = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField("Email", max_length=250, unique = True)
    RG = models.CharField(max_length=20, unique= True)
    CPF = models.CharField(max_length=20, unique = True)
    tipoUsuario = models.CharField(max_length= 20, choices=choices, null = True, blank = True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username",
                       "RG",
                       "CPF"]
    
    def __str__(self):
        return self.username