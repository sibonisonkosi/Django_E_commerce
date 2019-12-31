from django.urls import path
from . import views

urlpatterns =[
    path('', views.default, name = 'default'),
    path('item_list', views.item_list, name='item_list')
]