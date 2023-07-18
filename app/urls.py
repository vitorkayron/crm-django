from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo_produto/', views.novo_produto, name='novo_produto'),
    path('deletar_produto/<int:id>', views.deletar_produto, name='deletar_produto'),
    path('atualizar_produto/<int:id>', views.atualizar_produto, name='atualizar_produto'),
    path('venda/<int:id>', views.venda, name='venda')
]