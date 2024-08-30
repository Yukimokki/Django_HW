from django.contrib import admin
from django.urls import path, include
from catalog.views import home, contact
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
     path('', home),
     path('contacts/', contact)
]