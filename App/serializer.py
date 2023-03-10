from rest_framework.serializers import ModelSerializer
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PetTypeSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PetType


class StatusPetSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = StatusPet


class StatusOrderSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = StatusOrder


class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(PetSerializer, self).to_representation(instance)

        representation['category'] = CategorySerializer(instance.category, many=False).data
        representation['type'] = PetTypeSerializer(instance.type, many=False).data
        representation['status'] = StatusPetSerializer(instance.status, many=False).data

        return representation


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(OrderSerializer, self).to_representation(instance)

        representation['pets'] = PetSerializer(instance.pets, many=True).data
        representation['status'] = StatusOrderSerializer(instance.status, many=False).data

        return representation
