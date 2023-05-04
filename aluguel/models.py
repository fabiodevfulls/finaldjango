from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission, AbstractUser
from django.db import models


class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    fabricante = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    disponivel = models.BooleanField(default=True)
    placa = models.CharField(max_length=10)

    def __str__(self):
        return self.modelo


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.cliente} alugou o carro {self.carro}'


class Estatistica(models.Model):
    data = models.DateField()
    total_alugueis = models.IntegerField()
    total_receita = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Estatísticas para {self.data}'

    """
   Um gerenciador de usuários personalizado para criar e gerenciar contas de usuários.
    """

   


