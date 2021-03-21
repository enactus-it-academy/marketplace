from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from catalog import views as catalog
from user_account import views as user_account
from communication import views as feedbacks

router = routers.DefaultRouter()

router.register(r'users', user_account.UserViewSet)
router.register(r'suppliers', user_account.SupplierViewSet)
router.register(r'products', catalog.ProductViewSet)
router.register(r'feedbacks', feedbacks.FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
