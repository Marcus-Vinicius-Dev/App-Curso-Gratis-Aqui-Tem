from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('arquivosapp.urls')), # Inclua as rotas do aplicativo arquivosapp
    path('', api.urls),
]
