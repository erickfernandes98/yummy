from django import forms
from .models import Produto


class produtoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('id_produto', 'nome_produto', 'valor_produto', 'loja_produto')
        labels = {
            'id_produto': 'ID do Produto',
            'nome_produto': 'Nome do Produto',
            'valor_produto': 'Valor do Produto',
            'loja_produto': 'Loja'
        }

    def __init__(self, *args, **kwargs):
        super(produtoForm, self).__init__(*args, **kwargs)
        self.fields['loja_produto'].empty_label = "Selecione"