from . import views
from django.urls import path
from .views import  cart, checkout

urlpatterns = [

    path("cart/", views.cart, name="cart"),  
    path("checkout/", views.checkout, name="checkout"),
]