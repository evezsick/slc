from django.db import models

class SLC(models.Model):
    listas = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.listas}"
    
class Lista(models.Model):
    nome = models.ForeignKey(SLC, on_delete=models.CASCADE, related_name="nomes")

    def __str__(self):
        return f"{self.id} {self.nome}"

class Evento(models.Model):
    produto = models.ForeignKey(SLC, on_delete=models.CASCADE, related_name="produtos")
    preco = models.IntegerField(0)
    quantidade = models.IntegerField(0)

    def __str__(self):
        return f"ID:{self.id} Preço:{self.preco}  Produto:{self.compra}"