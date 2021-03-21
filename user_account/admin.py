from django.contrib import admin

from .models import User, Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
    list_display = ['user', 'phone_number', 'social_networks']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id', 'username', 'is_supplier', 'is_active']
