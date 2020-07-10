from django.db import models
from django.urls import reverse

# Create your models here.

class Setor(models.Model):
    nome = models.CharField(max_length=250)
    pausa_cafe = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('setor_editar', kwargs={'pk': self.pk})


class Funcionario(models.Model):
    SEXO = {
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
    }
    nome = models.CharField(max_length=250)
    sexo = models.CharField(max_length=250, choices=SEXO)
    data_nascimento = models.DateField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('funcionario_editar', kwargs={'pk': self.pk})
