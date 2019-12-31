from django.shortcuts import render
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView

class defaultView(ListView):
    model = Item
    template_name = 'my_app/index.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'my_app/product.html'
