from django.db import models

class Lista(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id} {self.nome}"

class Product(models.Model):
    produto = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"ID:{self.id} Preço:{self.preco}  Produto:{self.produto} Quantidade:{self.quantidade}"