from django.shortcuts import render
from .models import Item, OrderItem, Order

def default(request):

    context = {
        'items' : Item.objects.all()
    }
    return render(request, 'my_app/index.html', context)

def item_list(request):

    context = {
        'items' : Item.objects.all()
    }
    return render(request, 'my_app/item_list.html', context)