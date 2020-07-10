from django.db import models

# Create your models here.

class Setor(models.Model):
    nome = models.CharField(max_length=250)
    pausa_cafe = models.CharField(max_length=250)

class Funcionario(models.Model):    
    nome = models.CharField(max_length=250)
    sexo = models.CharField(max_length=250)
    data_nascimento = models.DateField