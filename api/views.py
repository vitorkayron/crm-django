from app.models import Produto, Venda, Saldo
from api.serializers import ProdutoSerializer, VendaSerializer, SaldoSerializer
from rest_framework import generics
class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendaList(generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaDetail(generics.RetrieveDestroyAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

