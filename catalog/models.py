from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from user_account.models import Supplier


class Container(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='containers')
    name = models.CharField('Название', max_length=80)
    location = models.CharField('Местоположение', max_length=100)


class Category(MPTTModel):
    name = models.CharField('Название', max_length=60, unique=True)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children',
                            verbose_name='Родитель')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    TRADE_CHOICES = [
        ('Оптовая', 'Оптовая'),
        ('Розничная', 'Розничная'),
        ('Оптово-розничная', 'Оптово-розничная')
    ]
    supplier = models.ForeignKey(Supplier,
                                 on_delete=models.CASCADE,
                                 related_name='products',
                                 verbose_name='Поставщик')
    container = models.ForeignKey(Container,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name='products',
                                  verbose_name='Контейнер')
    category = TreeForeignKey(Category,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name='products',
                              verbose_name='Категория')
    name = models.CharField("Название", max_length=255)
    image = models.ImageField("Изображение товара", upload_to="products/%Y/%m/%d", blank=True)
    trade = models.CharField("Торговля", choices=TRADE_CHOICES, max_length=16)
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Цена", default=0, max_digits=10, decimal_places=3)
    count = models.PositiveIntegerField('Количество', default=0)
    display = models.BooleanField('Отображение', default=True)

    def __str__(self):
        return self.name
