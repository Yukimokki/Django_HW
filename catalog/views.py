from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/start_page.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contact.html')

def catalog(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/products_list.html', context)

def product_card(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_card.html', context)