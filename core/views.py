# Todas as importações no topo do arquivo
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from contas.models import Cliente

# --- VIEWS PÚBLICAS ---

def home_view(request):
    """
    Renderiza o template index.html para a página inicial.
    """
    return render(request, 'index.html')

def produtos_view(request):
    """
    Renderiza o template produtos.html para a página de produtos.
    """
    return render(request, 'produtos.html')

def login_view(request):
    """
    Processa o login do cliente. Se for GET, mostra o formulário.
    Se for POST, valida as credenciais.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        # CORRIGIDO: O erro de digitação 'gert' foi trocado para 'get'.
        senha = request.POST.get('senha')

        try:
            # Tenta encontrar um cliente com o email fornecido
            cliente = Cliente.objects.get(email=email)

            # Verifica se a senha fornecida corresponde à senha no banco de dados
            if check_password(senha, cliente.senha):
                # Se a senha estiver correta, salva o ID do cliente na sessão
                request.session['cliente_id'] = cliente.id
                return redirect('painel_cliente') # Redireciona para o painel
            else:
                # Se a senha estiver incorreta
                error_message = "E-mail ou senha inválidos."
                return render(request, 'login.html', {'error_message': error_message})

        except Cliente.DoesNotExist:
            # Se o cliente com o e-mail não foi encontrado
            error_message = "E-mail ou senha inválidos."
            return render(request, 'login.html', {'error_message': error_message})

    # Se a requisição for GET, apenas mostra a página de login em branco
    return render(request, 'login.html')

def cadastro_cliente_view(request):
    """
    Esta view apenas renderiza o template de cadastro.
    A lógica de salvar o cadastro está no app 'contas'.
    """
    # Verifique se o caminho do seu template está correto.
    # Se ele estiver em 'templates/contas/cadastro_cliente.html', o nome está correto.
    return render(request, 'contas/cadastro_cliente.html')


# --- VIEWS PRIVADAS (SÓ PARA CLIENTES LOGADOS) ---

def painel_cliente_view(request):
    """
    Mostra o painel do cliente se ele estiver logado.
    Caso contrário, redireciona para a página de login.
    """
    if 'cliente_id' not in request.session:
        return redirect('login')

    try:
        cliente = Cliente.objects.get(id=request.session['cliente_id'])
        return render(request, 'painel_cliente.html', {'cliente': cliente})
    except Cliente.DoesNotExist:
        # Limpa uma sessão inválida (ex: cliente foi deletado)
        request.session.flush()
        return redirect('login')

def logout_view(request):
    """
    Remove os dados da sessão, efetivamente fazendo o logout do cliente.
    """
    request.session.flush()
    return redirect('login')