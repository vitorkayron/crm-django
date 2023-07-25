from rest_framework import serializers
from app.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'valor', 'quantidade_estoque']
