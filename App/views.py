from rest_framework.viewsets import ModelViewSet
from .serializer import *


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PetTypeViewSet(ModelViewSet):
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer


class StatusPetViewSet(ModelViewSet):
    queryset = StatusPet.objects.all()
    serializer_class = StatusPetSerializer


class StatusOrderViewSet(ModelViewSet):
    queryset = StatusOrder.objects.all()
    serializer_class = StatusOrderSerializer


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
