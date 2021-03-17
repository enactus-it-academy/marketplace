from typing import Container
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="product",
        verbose_name="Продавец"
    )

    

    image = models.ImageField(
        null=True, blank=True,
        upload_to="product_images",
        verbose_name="Изображение товара",
    )

    description = models.TextField(
        null=True, blank=True, verbose_name="Описание"
    )

    price = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=3, 
        verbose_name="Цена"
    )

    available = models.BooleanField(
        default=True, 
        verbose_name="Есть в наличии"
    )

    reviews = models.TextField(
        null=True, blank=True,
        verbose_name="Отзывы и вопросы"
    )



    def __str__(self):
        return self.name

    class Meta:
        verbose_name="товар"
        verbose_name_plural = "Товары"