from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField(default=0)
    faturamento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    qtd_vendas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

    def atualizar_faturamento(self):
        total_vendas = Venda.objects.filter(produto=self).aggregate(total=models.Sum('valor_venda'))['total']
        self.faturamento = total_vendas if total_vendas else 0
        self.save()

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    quantidade_vendida = models.PositiveIntegerField(default=0)
    data_venda = models.DateField(auto_now_add=True)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        if self.produto:
            return f"Venda de {self.produto.nome} - Quantidade: {self.quantidade_vendida} - Valor: {self.valor_venda}"
        else:
            return "Venda sem produto associado"

    def save(self, *args, **kwargs):
        if self.produto:
            self.valor_venda = self.produto.valor * self.quantidade_vendida
            self.produto.qtd_vendas += self.quantidade_vendida
            self.produto.atualizar_faturamento()  # Atualizar o faturamento no produto
        super().save(*args, **kwargs)

class Saldo(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, null=True)
    faturamento = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.produto.nome)