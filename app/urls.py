from django.urls import path
from . import views
from app.views import HomeListView

urlpatterns = [
    path('', HomeListView.as_view(), name="home"),
    path('novo_produto/', views.NovoProdutoCreateView.as_view(), name='novo_produto'),
    path('deletar_produto/<int:pk>', views.ProdutoDeleteView.as_view(), name='deletar_produto'),
    path('atualizar_produto/<int:pk>', views.ProdutoUpdateView.as_view(), name='atualizar_produto'),
    path('venda/<int:id>', views.venda, name='venda')
]