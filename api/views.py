from app.models import Produto, Venda, Saldo
from api.serializers import ProdutoSerializer, VendaSerializer, SaldoSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]


class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

class VendaList(generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]

class VendaDetail(generics.RetrieveDestroyAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]

class SaldoList(generics.ListCreateAPIView):
    queryset = Saldo.objects.all()
    serializer_class = SaldoSerializer
    permission_classes = [IsAuthenticated]

class SaldoDetail(generics.RetrieveDestroyAPIView):
    queryset = Saldo.objects.all()
    serializer_class = SaldoSerializer
    permission_classes = [IsAuthenticated]


