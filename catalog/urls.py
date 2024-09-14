from django.contrib import admin
from django.urls import path, include
from catalog.views import home, contact, catalog, product_card
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact, name="contacts"),
    path("catalog/", catalog, name="catalog"),
    path("product/<int:pk>", product_card, name="product_card"),
]
