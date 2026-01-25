from django.shortcuts import render
from .models import Order

def checkout(request):
    return render(request, 'orders/checkout.html')