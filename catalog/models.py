from django.db import models
from django.contrib.auth.models import User

from user_account.models import Supplier


class Product(models.Model):
    TRADE_CHOICES = [
        ('Оптовая', 'Оптовая'),
        ('Розничная', 'Розничная'),
        ('Оптово-розничная', 'Оптово-розничная')
    ]
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    name = models.CharField("Название", max_length=255)
    image = models.ImageField("Изображение товара", upload_to="products/%Y/%m/%d", blank=True)
    trade = models.CharField("Торговля", choices=TRADE_CHOICES, max_length=16)
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Цена", default=0, max_digits=10, decimal_places=3)
    count = models.PositiveIntegerField('Количество', default=0)
    display = models.BooleanField('Отображение', default=True)
