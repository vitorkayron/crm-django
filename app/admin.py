from django.contrib import admin
from .models import Produto, Saldo, Venda

# Register your models here.
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Saldo)
