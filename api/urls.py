from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

app_name = 'api'

urlpatterns = [
    path('produto/', views.ProdutoList.as_view()),
    path('produto/<int:pk>/', views.ProdutoDetail.as_view()),
    path('venda/', views.VendaList.as_view()),
    path('produto/<int:pk>', views.VendaDetail.as_view()),
    path('saldo/', views.SaldoList.as_view()),
    path('saldo/<int:pk>', views.SaldoDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)