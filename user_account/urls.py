from django.urls import path, include
from rest_framework import routers

from user_account import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'suppliers', views.SupplierViewSet)

urlpatterns = [
    path('', include(router.urls))
]
