from django.urls import path
from . import views

app_name = "my_app"
urlpatterns =[
    path('', views.defaultView.as_view(), name = 'default'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name='product')
]