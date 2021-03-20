from django.contrib import admin

from .models import Container, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'supplier', 'name', 'price']


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    model = Container
    list_display = ['id', 'supplier', 'name']
