from django.shortcuts import render


def products(request):
    return render(request, 'mainapp/products.html')


def product(request):
    return render(request, 'mainapp/product.html')
