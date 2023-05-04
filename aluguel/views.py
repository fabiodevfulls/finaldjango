
from django.contrib.auth import authenticate, login
from aluguel.forms import LoginForm
from .models import Cliente
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Carro, Cliente, Aluguel, Estatistica, CustomUser, CustomUserManager


class CarroListView(ListView):
    model = Carro
    template_name = 'carros/list.html'
    context_object_name = 'carros'


class CarroDetailView(DetailView):
    model = Carro
    template_name = 'carros/detail.html'
    context_object_name = 'carro'


class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/list.html'
    context_object_name = 'clientes'


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/detail.html'
    context_object_name = 'cliente'


class AluguelListView(ListView):
    model = Aluguel
    template_name = 'alugueis/list.html'
    context_object_name = 'alugueis'


class AluguelDetailView(DetailView):
    model = Aluguel
    template_name = 'alugueis/detail.html'
    context_object_name = 'aluguel'


class EstatisticaListView(ListView):
    model = Estatistica
    template_name = 'estatisticas/list.html'
    context_object_name = 'estatisticas'


class EstatisticaDetailView(DetailView):
    model = Estatistica
    template_name = 'estatisticas/detail.html'
    context_object_name = 'estatistica'


def aluguel(request):
    return render(request, 'base.html')

    
def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'aluguel/carros.html', {'carros': carros})


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
