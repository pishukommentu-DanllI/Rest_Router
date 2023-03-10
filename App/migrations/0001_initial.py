# Generated by Django 4.1.2 on 2023-03-10 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='PetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тип животоного')),
            ],
            options={
                'verbose_name': 'Тип животного',
                'verbose_name_plural': 'Типы животных',
            },
        ),
        migrations.CreateModel(
            name='StatusOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статусы заказов',
            },
        ),
        migrations.CreateModel(
            name='StatusPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус животного',
                'verbose_name_plural': 'Статусы животных',
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование животного')),
                ('photo', models.URLField(verbose_name='Фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.category', verbose_name='Категория')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.statuspet', verbose_name='Статус')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.pettype', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Животное',
                'verbose_name_plural': 'Животные',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, verbose_name='Количество')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('completed', models.BooleanField(verbose_name='Выполнено')),
                ('pets', models.ManyToManyField(to='App.pet', verbose_name='Животные')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.statusorder', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
