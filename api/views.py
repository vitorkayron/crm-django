from app.models import Produto, Venda, Saldo
from api.serializers import ProdutoSerializer, VendaSerializer, SaldoSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def faturamento_total(request):
    faturamento_total = Saldo.objects.aggregate(Sum('faturamento'))['faturamento__sum'] or 0

    return JsonResponse({'faturamento_total': faturamento_total})

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



