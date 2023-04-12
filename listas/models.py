from django.db import models

# Create your models here.

class SLC(models.Model):
    listas = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.listas}"

class Evento(models.Model):
    produto = models.ForeignKey(SLC, on_delete=models.CASCADE, related_name="produtos")
    preco = models.IntegerField(0)
    quantidade = models.IntegerField(0)

    def __str__(self):
        return f"{self.id}: {self.produto}"
