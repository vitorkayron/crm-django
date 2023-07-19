from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import Novo_Produto
from .models import Produto, Saldo, Venda
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

# # Create your views here.
# def home(request):
#     produtos = Produto.objects.all()
#     return render(request, 'home.html', {'produtos': produtos})

def calcular_faturamento():
    saldos = Saldo.objects.all()
    faturamento_total = sum(saldo.faturamento for saldo in saldos)
    return faturamento_total
            

class HomeListView(ListView):
    template_name = "home.html"
    model = Produto
    context_object_name = "produtos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faturamento_total = calcular_faturamento()
        context['faturamento_total'] = faturamento_total
        return context

class NovoProdutoCreateView(CreateView):
    template_name = "novo_produto.html"
    model = Produto
    form_class = Novo_Produto
    success_url = reverse_lazy("home")

# def novo_produto(request):
#     if request.method == 'GET':
#         form = Novo_Produto()
#         return render(request, 'novo_produto.html', {'form': form})
#     elif request.method == 'POST':
#         form = Novo_Produto(request.POST)
#         if form.is_valid():
#             form.save()
#             form = Novo_Produto()
#             return redirect('/')
#     else:
#         return render(request, 'novo_produto.html', {'form': form})
    

# def deletar_produto(request, id):
#     produto = Produto.objects.get(id=id)

#     if request.method == 'POST':
#         produto.delete()
#         return redirect('/')

#     return render(request,'deletar_produto.html', {'produto': produto})

class ProdutoDeleteView(DeleteView):
    template_name = "deletar_produto.html"
    model = Produto
    context_object_name = "produto"
    success_url = "/"

# def atualizar_produto(request, id):
#     produto = Produto.objects.get(id=id)
     
#     if request.method == "POST":
#         form = Novo_Produto(request.POST, instance=produto)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = Novo_Produto(instance=produto)

#     return render(request, 'atualizar_produto.html', {'produto': produto, 'form': form})

class ProdutoUpdateView(UpdateView):
    template_name = 'atualizar_produto.html'
    model = Produto
    form_class = Novo_Produto
    context_object_name = 'produto'

    def get_success_url(self):
        return '/'

def venda(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade'))

        if quantidade > produto.quantidade_estoque:
            messages.error(request, f"A quantidade solicitada ({quantidade}) é maior do que o estoque disponível ({produto.quantidade_estoque}).")
        else:
            produto.quantidade_estoque -= quantidade
            produto.save()

            venda = Venda(produto=produto, quantidade_vendida=quantidade, valor_venda=produto.valor * quantidade)
            venda.save()

            # Atualiza o saldo
            saldo, _ = Saldo.objects.get_or_create(produto=produto)
            saldo.faturamento += produto.valor * quantidade
            saldo.save()

            

            return redirect('/')

    return render(request, 'vendas.html', {'produto': produto})
 

            
