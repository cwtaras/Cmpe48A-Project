from django.shortcuts import render
from django.http import HttpResponse
from .models import item
# Create your views here.

def home(response):
    items = item.objects.all()
    return render(response, "main/home.html", {"items":items})

def cart(response):
    return render(response, "main/cart.html", {})

def create(response):
    return render(response, "main/create.html", {})   