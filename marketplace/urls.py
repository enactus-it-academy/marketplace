from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('user_account.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
