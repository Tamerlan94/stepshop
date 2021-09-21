from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.template.loader import render_to_string

# Create your views here.
from mainapp.models import Product
from .models import Basket


@login_required
def basket(request):
    if request.user.is_authenticated:
        basket_item = Basket.objects.filter(user=request.user)

        context = {
            'basket': basket_item,
        }

        return render(request, 'basketapp/basket.html', context)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, id=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    # Незнаю что за магия, но это сработало
    if request.is_ajax():
        basket_record = get_object_or_404(Basket, id=pk)
        product_total_price = basket_record.product.price * basket_record.quantity
        basket_record.delete()

        basket = Basket.objects.filter(user=request.user).order_by('product__category')

        context = {
            'basket': basket,
        }

        result = render_to_string('basketapp/includes/inc_basket_summary.html', context)

        return JsonResponse({'result': result, 'product_total_price': product_total_price})

    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        basket_item = Basket.objects.get(id=int(pk))

        if quantity > 0:
            basket_item.quantity = quantity
            basket_item.save()
        else:
            basket_item.delete()

        basket = Basket.objects.filter(user=request.user).order_by('product__category')

        context = {
            'basket': basket,
        }

        product_total_price = basket_item.product.price * basket_item.quantity

        # result = render_to_string('basketapp/includes/inc_basket_list.html', context)
        result = render_to_string('basketapp/includes/inc_basket_summary.html', context)

        return JsonResponse({'result': result, 'product_total_price': product_total_price})

