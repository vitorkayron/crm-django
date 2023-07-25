from rest_framework import serializers
from app.models import Produto, Venda

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'valor', 'quantidade_estoque']

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = "__all__"
