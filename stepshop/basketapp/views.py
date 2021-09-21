from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.
from mainapp.models import Product
from .models import Basket


def basket(request):
    if request.user.is_authenticated:
        basket_item = Basket.objects.filter(user=request.user)

        context = {
            'basket' : basket_item,
        }

        return render(request, 'basketapp//basket.html', context)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_add(request, pk):
    product = get_object_or_404(Product, id=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    return render(request, 'basketapp//basket.html')
