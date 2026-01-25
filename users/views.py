from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User

def register_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        full_name = request.POST.get("full_name")

        if User.objects.filter(phone=phone).exists():
            return render(request, "users/register.html", {"error": "Bu telefon ro'yxatdan o'tgan!"})

        user = User.objects.create_user(phone=phone, password=password, full_name=full_name)
        login(request, user)
        return redirect("main:home")  # TO‘G‘RI!

    return render(request, "users/register.html")

def login_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        user = authenticate(request, phone=phone, password=password)
        if user:
            login(request, user)
            return redirect("main:home")  # TO‘G‘RI!
        else:
            return render(request, "users/login.html", {"error": "Telefon yoki parol noto'g'ri!"})

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("main:home")