from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product, ProductCategory


def products(request, pk=None):
    title = 'продукты | каталог'
    products_all = Product.objects.all()
    categories = ProductCategory.objects.all()
    category = {'name': 'продукты'}

    basket = []

    if pk is not None:
        products_all = Product.objects.filter(category__id=pk)
        category = get_object_or_404(ProductCategory, id=pk)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'products': products_all,
        'categories': categories,
        'category': category,
        'pk': pk,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'продукт'

    links_menu = ProductCategory.objects.all()
    product_item = get_object_or_404(Product, id=pk)
    all_products = Product.objects.filter(category=product_item.category)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product_item,
        'similar_products': all_products,
    }

    return render(request, 'mainapp/product.html', context)
