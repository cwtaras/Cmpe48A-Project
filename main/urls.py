from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("cart", views.cart, name="cart"),
path("payment", views.payment, name="home"),
path("shipment", views.shipment, name="home")
]