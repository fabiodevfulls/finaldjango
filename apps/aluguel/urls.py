from django.urls import path
from apps.aluguel.views import (
    aluguel, detalhar_carro, cadastro_carro, editar_carro, deletar_carro, filtro, buscar, detalhar_aluguel, realizar_aluguel
)

urlpatterns = [
    path('', aluguel, name='index'),
    path('detalhar_carro/<int:carro_pk>/',detalhar_carro, name='detalhar_carro'),
    path('buscar/', buscar, name='buscar'),
    path('cadastro_carro/', cadastro_carro, name='cadastro_carro'),
    path('editar_carro/<int:carro_pk>/', editar_carro, name='editar_carro'),
    path('deletar_carro/<int:carro_pk>/', deletar_carro, name='deletar_carro'),
    path('filtro/<str:categoria>/', filtro, name='filtro'),
    path('realizar_aluguel/<int:carro_pk>/',realizar_aluguel, name='realizar_aluguel'),
    path('detalhar_aluguel/<int:pk>/', detalhar_aluguel, name='detalhar_aluguel'),
]
