from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class PetType(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тип животоного')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животных'


class StatusPet(models.Model):
    name = models.CharField(max_length=30, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус животного'
        verbose_name_plural = 'Статусы животных'


class StatusOrder(models.Model):
    name = models.CharField(max_length=30, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'


class Pet(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование животного')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    photo = models.URLField(verbose_name='Фото')
    type = models.ForeignKey(PetType, verbose_name='Тип', on_delete=models.CASCADE)
    status = models.ForeignKey(StatusPet, verbose_name='Статус', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'


class Order(models.Model):
    pets = models.ManyToManyField(Pet, verbose_name='Животные')
    count = models.IntegerField(default=1, verbose_name='Количество')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    status = models.ForeignKey(StatusOrder, verbose_name='Статус', on_delete=models.CASCADE)
    completed = models.BooleanField(verbose_name='Выполнено')

    def __str__(self):
        return f'Заказ с {",".join(map(lambda x: str(x), self.pets.all()))} на {self.date}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


@receiver(m2m_changed, sender=Order.pets.through)
def my_handler(sender, instance, action, **kwargs):
    instance.count = len(instance.pets.all())
    instance.save()

