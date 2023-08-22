from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import Novo_Produto
from .models import Produto, Saldo, Venda
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from accounts.forms import LoginForm
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                    'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    


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

class ProdutoDeleteView(DeleteView):
    template_name = "deletar_produto.html"
    model = Produto
    context_object_name = "produto"
    success_url = "/home"


class ProdutoUpdateView(UpdateView):
    template_name = 'atualizar_produto.html'
    model = Produto
    form_class = Novo_Produto
    context_object_name = 'produto'

    def get_success_url(self):
        return '/home'

def venda(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        quantidade = request.POST.get('quantidade')

        try:
            quantidade = int(quantidade)
        except ValueError:
            messages.error(request, "A quantidade informada não é válida.")
            return redirect('home')

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

            produto.atualizar_faturamento()  # Atualizar o faturamento no produto

            return redirect('home')

    return render(request, 'vendas.html', {'produto': produto})
