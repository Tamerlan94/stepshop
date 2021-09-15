from django.shortcuts import render


def products(request):
    title = 'продукты | каталог'

    links_menu = [
        {'href': 'product_all', 'name': 'все'},
        {'href': 'product_shoes', 'name': 'обувь'},
        {'href': 'product_pants', 'name': 'штаны'},
        {'href': 'product_phones', 'name': 'смартфоны'},
    ]

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context)


def product(request):
    return render(request, 'mainapp/product.html')
