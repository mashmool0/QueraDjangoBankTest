from django.http import JsonResponse, Http404
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404


def checkout(request, order_pk):
    order = get_object_or_404(Order, id=order_pk)
    order_list = OrderItem.objects.filter(order=order)
    total_price = 0
    for item in order_list:
        total_price += item.product.price * item.quantity

    return JsonResponse({"total_price": f"{total_price:.2f}"})
