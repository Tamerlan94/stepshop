from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def get_basket(user_):
    if user_.is_authenticated:
        return Basket.objects.filter(user=user_)
    else:
        return []


def index(request):

    title = 'главная'
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(category__is_active=True)

    basket = get_basket(request.user)

    context = {
        'title': title,
        'categories': categories,
        'products': products,
        'basket': basket,
    }

    return render(request, 'stepshop/index.html', context)


def contacts(request):

    title = 'контакты'

    basket = get_basket(request.user)

    context = {
        'title': title,
        'basket': basket,
    }

    return render(request, 'stepshop/contact.html', context)


def about(request):

    title = 'о нас'

    basket = get_basket(request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'stepshop/about.html', context)
