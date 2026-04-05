from django.shortcuts import render
from .models import Product
# Create your views here.
def products(request):
    return render(request, 'products/products.html',{'ps':Product.objects.all()})


def product(request):
    return render(request, 'products/product.html')
