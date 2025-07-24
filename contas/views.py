
from django.shortcuts import render, redirect
from rest_framework import viewsets 
from .models import Cliente 
from .serializers import ClienteSerializer 
from .forms import ClienteForm

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que os clientes sejam visualizados ou editados.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            dados_limpos = form.cleaned_data
            endereco_completo = f"{dados_limpos['rua']}, {dados_limpos['numero']} - {dados_limpos['bairro']}, {dados_limpos['estado']} ({dados_limpos['uf']})"

            novo_cliente = Cliente(
                nome=dados_limpos['nome'],
                cpf=dados_limpos['cpf'],
                telefone=dados_limpos['telefone'],
                email=dados_limpos['email'],
                senha=dados_limpos['senha'],
                endereco=endereco_completo
            )
            novo_cliente.save()
            
            return redirect('contas:pagina_de_sucesso')
    else:
        form = ClienteForm()

    return render(request, 'contas/cadastro_cliente.html', {'form': form})


def pagina_de_sucesso(request):
    return render(request, 'contas/sucesso.html')