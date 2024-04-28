# arquivosapp/urls.py
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    # Adicione outras rotas específicas do aplicativo aqui
]
