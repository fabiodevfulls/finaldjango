from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Carro
from .serializers import CarroSerializer


@receiver(post_save, sender=Carro)
def carro_post_save(sender, instance, created, **kwargs):
    if created:
        # Lógica a ser executada quando um novo carro for salvo
        serializer = CarroSerializer(instance)
        serialized_data = serializer.data
        print("Um novo carro foi salvo:", serialized_data)
    else:
        # Lógica a ser executada quando um carro existente for atualizado
        serializer = CarroSerializer(instance)
        serialized_data = serializer.data
        print("Um carro existente foi atualizado:", serialized_data)
