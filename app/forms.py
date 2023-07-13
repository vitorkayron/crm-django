from django import forms
from .models import Produto


class Novo_Produto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"