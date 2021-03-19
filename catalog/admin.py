from django.contrib import admin

from .models import Product


@admin.register(Product)
class CatalogAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'supplier', 'name', 'price']
