

from .models import Aluguel, Carro
from .forms import AluguelForm
from .models import Aluguel
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from apps.aluguel.models import Carro,Aluguel
from apps.aluguel.forms import CarroForms,AluguelForm
from django.shortcuts import render



def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carro/listar.html', {"carros": carros})




def aluguel(request):
    if not request.user.is_authenticated:
        messages.error(request, 'usuario não logado')
        return redirect('login')
    carros = Carro.objects.order_by("fabricante").filter(publicada=True)
    return render(request, 'index.html', {"cards": carros})


def detalhar_carro(request, foto_id):
    carro=get_object_or_404(Carro, pk = foto_id)
    return render(request, 'carros/detalhar_carro.html', {"carro": carro})


def cadastro_carro(request):
    if not request.user.is_authenticated:
        messages.error(request, 'usuario não logado')
        return redirect('login')
    form= CarroForms
    if request.method == 'POST':
        form= CarroForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,' o novo carro foi cadstrado')
            return redirect('index')
    return render(request, "cadastro_carro.html", {'form': form})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    carros = Carro.objects.order_by(
        "data_compra").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            carros = Carro.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards": carros})
def editar_carro(request,foto_id):
    carro= Carro.objects.get(id=foto_id)
    form = CarroForms(instance= carro)
    if request.method == 'POST':
        form= CarroForms(request.POST, request.FILES, instance= carro)
        if form.is_valid():
            form.save()
            messages.success(request, '  carro editado com sucesso')
            return redirect('index')
    return render(request,"editar_carro.html", {'form': form,'foto_id': foto_id})

def deletar_carro(request,foto_id):
    carro = Carro.objects.get(id=foto_id)
    carro.delete()
    messages.success(request, 'carro excluída com sucesso.')
    return redirect('index')
    
def filtro(request):
    carros = Carro.objects.order_by("fabricante").filter(publicada=True)
    return render(request, 'index.html', {"cards": carros})


def realizar_aluguel(request, carro_pk):
    carro = Carro.objects.get(pk=carro_pk)

    if request.method == 'POST':
        form = AluguelForm(request.POST)
        if form.is_valid():
            aluguel = form.save(commit=False)
            aluguel.carro = carro
            aluguel.usuario = request.user
            aluguel.save()
            return redirect('detalhar_aluguel', aluguel.pk)
    else:
        form = AluguelForm()

    return render(request, 'realizar_aluguel.html', {'form': form, 'carro': carro})


def detalhar_aluguel(request, pk):
    aluguel = get_object_or_404(Aluguel, pk=pk)
    return render(request, 'detalhar_aluguel.html', {'aluguel': aluguel})

