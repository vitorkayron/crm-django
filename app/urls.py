from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo_produto/', views.novo_produto, name='novo_produto')
]