from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=50, name='Имя покупателя')  # username аккаунта
    balance = models.DecimalField(max_digits=10, decimal_places=2, name='Баланс')
    age = models.IntegerField(name='Возраст')

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=50, name='Название игры')
    cost = models.DecimalField(max_digits=10, decimal_places=2, name='Цена')
    size = models.DecimalField(max_digits=10, decimal_places=2, name='Размер файлов игры')
    description = models.TextField(name='Описание')
    age_limited = models.BooleanField(default=False, name='Ограничение возраста 18+')
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title
