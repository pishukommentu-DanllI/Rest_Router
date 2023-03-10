from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('category', CategoryViewSet)
router.register('PetType', PetTypeViewSet)
router.register('StatusPet', StatusPetViewSet)
router.register('StatusOrder', StatusOrderViewSet)
router.register('pets', PetViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
