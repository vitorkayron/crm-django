from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=True)
    valor = models.DecimalField(max_digits=1000, decimal_places=3) 
    quantidade_estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome