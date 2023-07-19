from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Produto, Saldo, Venda


admin.site.unregister(Group)

# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'quantidade_estoque')
    search_fields = ('nome', )
    list_filter = ('nome', )

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'valor_venda', 'quantidade_vendida')
    search_fields = ('produto', 'data_venda')
    list_filter = ('produto', )
    ordering = ('data_venda', 'quantidade_vendida', 'valor_venda')
    readonly_fields=('data_venda', 'produto', 'quantidade_vendida', 'valor_venda')


@admin.register(Saldo)
class Saldo(admin.ModelAdmin):
    list_display = ('produto', 'faturamento')
    search_fields = ('produto',)
    list_filter = ('produto', 'faturamento')
    ordering = ('faturamento', )   
    readonly_fields=('produto', 'faturamento' )
