from django.shortcuts import render, redirect
from .forms import Novo_Produto
from .models import Produto

# Create your views here.
def home(request):
    return render(request, 'home.html')
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