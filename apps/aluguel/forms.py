from .models import Aluguel
from django import forms
from apps.aluguel.models import Carro,Aluguel




class CarroForms(forms.ModelForm):
    class Meta:
        model= Carro
        exclude = ['publicada ','data_compra']
        labels= {
           'usuario': 'Usuário',
            
        }

        data_compra= forms.DateInput(
            
            format='%d/%m/%Y',
            attrs={
                'type': 'date',
                'class': 'form-control'
            })

        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'fabricante': forms.Select(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'ano' : forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            
        }


class AluguelForms(forms.ModelForm):
    class Meta:
        model = Aluguel
        exclude = ['devolucao']
        labels = {
            'codigo': 'Código',
            'data_aluguel': 'Data de aluguel',
            'data_devolucao': 'Data de devolução',
            'valor': 'Valor',
            'devolucao': 'Devolvido',
            'carro': 'Carro',
            'usuario': 'Cliente',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'data_aluguel': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_devolucao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'carro': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }

        
