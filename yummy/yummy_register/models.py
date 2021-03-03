from django.db import models

# Create your models here.


class Loja(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    id_produto = models.CharField(max_length=100)
    nome_produto = models.CharField(max_length=100)
    loja_produto = models.ForeignKey(Loja, on_delete=models.CASCADE)
    valor_produto = models.CharField(max_length=10)
