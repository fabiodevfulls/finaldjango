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


class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = '__all__'
        