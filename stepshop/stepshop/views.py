from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):

    title = 'главная'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    context = {
        'title': title,
        'categories': categories,
        'products': products,
    }

    return render(request, 'stepshop/index.html', context)


def contacts(request):

    title = 'контакты'

    context = {
        'title': title,
    }

    return render(request, 'stepshop/contact.html', context)


def about(request):

    title = 'о нас'

    context = {
        'title': title,
    }
    return render(request, 'stepshop/about.html', context)
