from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.decorators.cache import cache_page

from users.views import UserLoginView
from catalog.views import ProductListView, ProductDetailView, home, contact, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns =[
    path('', home,name='home'),
    path("contacts/", contact, name="contacts"),
    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('catalog/product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('catalog/product/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    #path('accounts/login/', UserLoginView.as_view(template_name="users/login.html"), name="login"),
    path("accounts/login/", LoginView.as_view(template_name="users/login.html"), name="login"),
]

# urlpatterns = [
#     path("", home, name="home"),
#     path("contacts/", contact, name="contacts"),
#     path("catalog/", catalog, name="catalog"),
#     path("product/<int:pk>", product_card, name="product_card"),
# ]
