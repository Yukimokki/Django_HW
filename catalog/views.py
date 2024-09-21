from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object=super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ("id", "name", "price", "category", "views_counter")
    success_url = reverse_lazy('product:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("id", "name", "price", "category",)
    success_url = reverse_lazy('product:products_list')

    def get_success_url(self):
        return reverse('product:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:products_list')

def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/home.html", context)
#
#
# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("phone")
#         message = request.POST.get("message")
#         print(f"You have new message from {name}({email}): {message}")
#     return render(request, "catalog/contact.html")
#
#
# def catalog(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "catalog/products_list.html", context)
#
#
# def product_card(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "catalog/product_card.html", context)
