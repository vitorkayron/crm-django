from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import Novo_Produto
from .models import Produto, Saldo
from django.contrib import messages
# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos': produtos})
# def novo_produto(request):
#     if request.method == "POST":

def novo_produto(request):
    if request.method == 'GET':
        form = Novo_Produto()
        return render(request, 'novo_produto.html', {'form': form})
    elif request.method == 'POST':
        form = Novo_Produto(request.POST)
        if form.is_valid():
            form.save()
            form = Novo_Produto()
            return redirect('/')
    else:
        return render(request, 'novo_produto.html', {'form': form})
    
def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('/')

    return render(request,'deletar_produto.html', {'produto': produto})

def atualizar_produto(request, id):
    produto = Produto.objects.get(id=id)
     
    if request.method == "POST":
        form = Novo_Produto(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Novo_Produto(instance=produto)

    return render(request, 'atualizar_produto.html', {'produto': produto, 'form': form})

def venda(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade'))

        if quantidade > produto.quantidade_estoque:
            messages.error(request, f"A quantidade solicitada ({quantidade}) é maior do que o estoque disponível ({produto.quantidade_estoque}).")
        else:
            produto.quantidade_estoque -= quantidade
            produto.save()

            # Atualiza o saldo
            saldo, _ = Saldo.objects.get_or_create(produto=produto)
            saldo.faturamento += produto.valor * quantidade
            saldo.save()

            return redirect('/')

    return render(request, 'vendas.html', {'produto': produto})
 
            
            
