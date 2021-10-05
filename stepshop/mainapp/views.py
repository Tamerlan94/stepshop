from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from basketapp.models import Basket
from .models import Product, ProductCategory


def get_basket(user_):
    if user_.is_authenticated:
        return Basket.objects.filter(user=user_)
    else:
        return []


def products(request, pk=None, page=1):
    title = 'продукты | каталог'
    products_all = Product.objects.filter(category__is_active=True, is_active=True)  # all()
    categories = ProductCategory.objects.all()
    category = {'name': 'продукты'}

    if pk is not None:
        products_all = Product.objects.filter(category__id=pk, is_active=True)
        category = get_object_or_404(ProductCategory, id=pk)
        if not category.is_active:
            return HttpResponseRedirect(reverse('products:index'))

    basket = get_basket(request.user)

    paginator = Paginator(products_all, 1)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'products': products_all,
        'products_p': paginator,
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
    all_products = Product.objects.filter(category=product_item.category).exclude(id=product_item.id)

    category = product_item.category

    if not category.is_active or not product_item.is_active:
        return HttpResponseRedirect(reverse('products:index'))

    basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product_item,
        'similar_products': all_products,
        'basket': basket,
    }

    return render(request, 'mainapp/product.html', context)
