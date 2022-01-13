from django.shortcuts import render
from django.http import HttpResponse
from .forms import Card
import json
from django.http import HttpResponseRedirect
from .helpers.get_products_cloud_func import get_products
from .helpers.show_basket_cloud_func import show_basket
from .helpers.remove_product_from_basket import remove_basket
from .helpers.total_price import get_total_price
from .helpers.insert_to_basket_cloud_func import add_basket
from .helpers.publish_pubsub import make_payment

# Create your views here.

def home(response):
    products = get_products()
    if 'add' in response.POST:
        product = response.POST.get('add')
        print(product)
        add_basket(product)
    return render(response, "main/home.html", {"products":products})

def cart(response):
    products = show_basket()
    price = get_total_price()
    if 'remove' in response.POST:
        product = response.POST.get('remove')
        remove_basket(product)
    return render(response, "main/cart.html", {"products":products, "price":price})

def payment(response):
    if response.method == "POST" or None:
        form = Card(response.POST or None)
        if form.is_valid():
            returned = make_payment()
            if returned == "OK":
                return HttpResponseRedirect("/shipment")
            else:
                form = Card()
                return render(response, "main/payment.html", {"form":form})
        else:
            form = Card()
            return render(response, "main/payment.html", {"form":form})

    return render(response, "main/payment.html", {})

def shipment(response):
     return render(response, "main/shipment.html", {})

  