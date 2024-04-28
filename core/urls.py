from django.contrib import admin
from django.urls import path
from .api import api
from arquivosapp.views import home # Corrigido aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),
    path('', home, name='home')
]
