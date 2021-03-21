from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter

from .models import Container, Category, Product


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    model = Container
    list_display = ['id', 'supplier', 'name']


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    model = Category
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Добавить совокупное количество товаров
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Добавить не совокупное количество товаров
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_count',
            cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Связанные товары (Для конкретной категории)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Связанные товары'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'supplier', 'name', 'price']
