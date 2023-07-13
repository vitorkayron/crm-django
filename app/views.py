from django.shortcuts import render, redirect, HttpResponse
from .forms import Novo_Produto

# Create your views here.
def home(request):
    return render(request, 'base.html')
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
