from django import forms
from .models import Product, Lista

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['produto', 'preco', 'quantidade']

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['nome']