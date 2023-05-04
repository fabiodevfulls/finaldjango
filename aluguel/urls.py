from django.urls import path
from aluguel import views
from django.urls import path
from aluguel.views import (
    CarroListView, CarroDetailView,
    ClienteListView, ClienteDetailView,
    AluguelListView, AluguelDetailView,
    EstatisticaListView, EstatisticaDetailView,
    login_usuario,

)

app_name = 'aluguel'

urlpatterns = [
    path('carros/', CarroListView.as_view(), name='carro_list'),
    path('carros/<int:pk>/', CarroDetailView.as_view(), name='carro_detail'),
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('alugueis/', AluguelListView.as_view(), name='aluguel_list'),
    path('alugueis/<int:pk>/', AluguelDetailView.as_view(), name='aluguel_detail'),
    path('estatisticas/', EstatisticaListView.as_view(), name='estatistica_list'),
    path('login/', login_usuario, name='login'),
    
    path('estatisticas/<int:pk>/', EstatisticaDetailView.as_view(),
         name='estatistica_detail'),
]


urlpatterns = [
    path('', views.aluguel, name= 'base'),
    path('carros/', views.lista_carros, name='carro'),
   
]
