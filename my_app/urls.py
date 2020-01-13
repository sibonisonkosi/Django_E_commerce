from django.urls import path
from . import views

app_name = "my_app"
urlpatterns =[
    path('', views.defaultView.as_view(), name = 'default'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart')
]