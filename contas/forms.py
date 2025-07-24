from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    
    rua = forms.CharField(max_length=200, required=True)
    numero = forms.CharField(max_length=20, required=True, label="Nº")
    bairro = forms.CharField(max_length=100, required=True)
    uf = forms.CharField(max_length=2, required=True, label="UF")
    estado = forms.CharField(max_length=100, required=True) 

 
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")

    class Meta:
        model = Cliente
       
        fields = ['nome', 'cpf', 'telefone', 'email', 'senha']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
       
        self.fields['nome'].label = "Nome Completo"
        
        self.order_fields(['nome', 'cpf', 'telefone', 'email', 'rua', 'numero', 'bairro', 'uf', 'estado', 'senha'])