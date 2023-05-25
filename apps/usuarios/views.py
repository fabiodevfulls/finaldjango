from django.shortcuts import render, redirect
from apps.usuarios.forms import loginForms,cadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def login(request):
    form = loginForms()
    if request.method == 'POST':
        form = loginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = cadastroForms()
    if request.method == 'POST':
        form = cadastroForms(request.POST)
        if form.is_valid():
            senha_1 = form.cleaned_data['senha_1']
            senha_2 = form.cleaned_data['senha_2']

            if senha_1 != senha_2:
                messages.error(request, 'As senhas não são iguais')
                return redirect('cadastro')

            nome = form.cleaned_data['nome_cadastro']
            email = form.cleaned_data['email']

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome, email=email, password=senha_1)
            usuario.save()

            messages.success(request, 'Cadastro efetuado com sucesso')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')

"""""
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/listar.html', {"clientes": clientes})


def detalhar_cliente(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        messages.error(request, 'Cliente não encontrado')
        return redirect('listar_clientes')

    return render(request, 'cliente/detalhar.html', {"cliente": cliente})
"""