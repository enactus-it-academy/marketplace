from django.contrib import admin
from .models import *

@admin.register(Product)
class CatalogAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'user', 'image', 'description',  'price' , 'available', 'reviews' ]
