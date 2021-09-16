from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


def products(request, pk=None):
    title = 'продукты | каталог'
    products_all = Product.objects.all()
    categories = ProductCategory.objects.all()
    category = {'name': 'продукты'}

    if pk is not None:
        products_all = Product.objects.filter(category__id=pk)
        category = get_object_or_404(ProductCategory, id=pk)

    context = {
        'title': title,
        'products': products_all,
        'categories': categories,
        'category': category,
        'pk': pk,
    }

    return render(request, 'mainapp/products.html', context)


def product(request):
    return render(request, 'mainapp/product.html')
