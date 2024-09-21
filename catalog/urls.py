from django.contrib import admin
from django.urls import path, include
from catalog.views import ProductListView, ProductDetailView, home, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns =[
    path('', home,name='home'),
    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('catalog/product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/product/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/product/<int:pk>/uptade', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]

# urlpatterns = [
#     path("", home, name="home"),
#     path("contacts/", contact, name="contacts"),
#     path("catalog/", catalog, name="catalog"),
#     path("product/<int:pk>", product_card, name="product_card"),
# ]
