from django.urls import path
from apps.aluguel.views import \
    aluguel, detalhar_carro, cadastro_carro, editar_carro, deletar_carro, filtro, buscar, realizar_aluguel_carro, lista_aluguel, realizar_aluguel

urlpatterns = [
    path('',aluguel, name= 'index'),
    path('detalhar_carro<int:foto_id>',detalhar_carro, name='detalhar_carro'),
    path('buscar', buscar, name='buscar'),
    path('cadastro_carro', cadastro_carro, name='cadastro_carro'),
    path('editar-carro/<int:foto_id>', editar_carro, name='editar_carro'),
    path('deletar-carro<int:foto_id>', deletar_carro, name='deletar_carro'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
    path('realizar_aluguel<int:carro_pk>',realizar_aluguel_carro, name='realizar_aluguel_carro'),
    path('realizar_aluguel/', realizar_aluguel, name='realizar_aluguel'),
    path('lista-aluguel/', lista_aluguel, name='lista_aluguel'),
    

]
