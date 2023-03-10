from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)


@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)


@admin.register(StatusOrder, StatusPet)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'photo', 'type', 'status')
    list_editable = ('name', 'category', 'photo', 'type', 'status')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'date', 'status', 'completed')
    list_editable = ( 'status', 'completed')
