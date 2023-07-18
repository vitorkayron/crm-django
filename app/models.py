from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=1000, decimal_places=3) 
    quantidade_estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome
    
class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_vendida = models.PositiveIntegerField(default=0)
    data_venda = models.DateField(auto_now_add=True)
    valor_venda = models.DecimalField(max_digits=1000, decimal_places=3, default=0)

    def __str__(self):
        return f"Saldo de {self.produto.nome} - {self.quantidade_vendida} vendido(s)"

    def save(self, *args, **kwargs):
        self.valor_venda = self.produto.valor * self.quantidade_vendida
        super().save(*args, **kwargs)
        
class Saldo(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, null=True)
    faturamento = models.DecimalField(max_digits=1000, decimal_places=3, default=0)

    def __str__(self):
        return str(self.faturamento)

    def atualizar_saldo(self):
        total_vendas = Venda.objects.filter(produto=self.produto).aggregate(total=models.Sum('valor_venda'))['total']
        self.faturamento = total_vendas if total_vendas else 0
        self.save()