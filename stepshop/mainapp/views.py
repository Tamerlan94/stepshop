from django.shortcuts import render
from .models import Product, ProductCategory


def products(request):
    title = 'продукты | каталог'
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'title': title,
        'products': products,
        'categories': categories,
    }

    return render(request, 'mainapp/products.html', context)


def product(request):
    return render(request, 'mainapp/product.html')
