"""это urls.py основной, проекта, а у приложения catalog - свой urls.py"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('catalog.urls'))
]
