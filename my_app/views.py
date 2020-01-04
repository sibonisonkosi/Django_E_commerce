from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.utils import timezone

class defaultView(ListView):
    model = Item
    template_name = 'my_app/index.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'my_app/product.html'

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    # The below line is a tuple. It return order_item if it exist or created variable holds the created order_item if it does not exist.
    # This is done to ensure the same the same odered item doesn't apear many times in the list bust increase only quantity
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    # Getting orders which are not completed
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date = ordered_date)
        order.items.add(order_item)
    return redirect("my_app:product",slug=slug)