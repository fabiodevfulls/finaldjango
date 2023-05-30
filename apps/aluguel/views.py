from django.shortcuts import render, redirect, get_object_or_404
from .models import Carro, Aluguel
from .forms import AluguelForms, CarroForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CarroSerializer, AluguelSerializer


def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carro/listar.html', {"carros": carros})


def aluguel(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    carros = Carro.objects.order_by("fabricante").filter(publicada=True)
    return render(request, 'index.html', {"cards": carros})


def detalhar_carro(request, carro_pk):
    carro = Carro.objects.get(pk=carro_pk)
    return render(request, 'carros/detalhar_carro.html', {"carro": carro})


@login_required
def cadastro_carro(request):
    form = CarroForms()
    if request.method == 'POST':
        form = CarroForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O novo carro foi cadastrado.')
            return redirect(reverse_lazy('index'))
    return render(request, "cadastro_carro.html", {'form': form})


@login_required
def buscar(request):
    carros = Carro.objects.order_by("data_compra").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            carros = carros.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards": carros})


@login_required
def editar_carro(request, carro_pk):
    carro = get_object_or_404(Carro, pk=carro_pk)

    if request.method == "POST":
        form = CarroForms(request.POST, request.FILES,
                          instance=carro)  # Adicionado request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, 'Carro alterado com sucesso.')
            return redirect(reverse_lazy('detalhar_carro', kwargs={'carro_pk': carro_pk}))
    else:
        form = CarroForms(instance=carro)

    context = {'form': form, 'carro_pk': carro_pk}
    return render(request, 'editar_carro.html', context)


@login_required
def deletar_carro(request, carro_pk):
    carro = get_object_or_404(Carro, id=carro_pk)
    carro.delete()
    messages.success(request, 'Carro excluído com sucesso.')
    return redirect(reverse_lazy('index'))


def filtro(request, categoria):
    carros = Carro.objects.order_by("fabricante").filter(
        fabricante=categoria, publicada=True)
    return render(request, 'index.html', {"cards": carros})


def realizar_aluguel(request, carro_pk):
    carro = get_object_or_404(Carro, pk=carro_pk)

    if request.method == "POST":
        form = AluguelForms(request.POST)
        if form.is_valid():
            aluguel = form.save(commit=False)
            aluguel.carro = carro
            # Defina o valor do campo "devolucao"

            aluguel.save()
            messages.success(request, 'Aluguel realizado com sucesso')
            return redirect(reverse_lazy('detalhar_aluguel', kwargs={'pk': aluguel.pk}))
    else:
        form = AluguelForms(initial={'carro': carro})

    context = {'carro_pk': carro_pk, 'form': form}
    return render(request, 'aluguel/realizar_aluguel.html', context)


def detalhar_aluguel(request, pk):
    aluguel = get_object_or_404(Aluguel, pk=pk)
    return render(request, 'aluguel/detalhar_aluguel.html', {'aluguel': aluguel})


class CarroSerializer(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
