from rest_framework import serializers
from app.models import Produto, Venda, Saldo

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'valor', 'quantidade_estoque']

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = "__all__"

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saldo
        fields = "__all__"
