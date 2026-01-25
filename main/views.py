from django.shortcuts import render
from .models import Image


def home(request): 
    image = Image.objects.all() 
    return render(request, "main/home.html",{"image":image})

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")