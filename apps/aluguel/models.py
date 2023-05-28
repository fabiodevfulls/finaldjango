from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Carro(models.Model):
    OPCOES_CATEGORIA = [
        ("Chevrolet", "Chevrolet"),
        ("Volkswagen", "Volkswagen"),
        ("Fiat", "Fiat"),
        ("Ford", "Ford"),
        ("Renault", "Renault"),
        ("Toyota", "Toyota"),
        ("Honda", "Honda"),
        ("Hyundai", "Hyundai"),
    ]
    ANO = [(str(i), str(i)) for i in range(1990, 2025)]
    modelo = models.CharField(max_length=10, null=False, blank=False)
    ano = models.CharField(max_length=100, choices=ANO,
                           default=str(datetime.now().year))
    fabricante = models.CharField(
        max_length=100, choices=OPCOES_CATEGORIA, default='')
    placa = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    data_compra = models.DateTimeField(default=datetime.now, blank=False)
    publicada = models.BooleanField(default=True)
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='carros')

    def __str__(self):
        return "{} - {}".format(self.modelo, self.placa)



class Aluguel(models.Model):
    codigo = models.CharField("Código", max_length=100)
    data_aluguel = models.DateTimeField(default=datetime.now, blank=False)
    data_devolucao = models.DateTimeField(default=datetime.now, blank=False)
    valor = models.DecimalField("Valor", max_digits=15, decimal_places=2)
    devolucao = models.BooleanField(default=True)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='alugueis')

    def __str__(self):
        return "{} - {} - {}".format(self.codigo, self.usuario.username, self.carro.modelo)
