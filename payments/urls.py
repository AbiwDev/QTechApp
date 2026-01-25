from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    path('success/', views.payment_success, name='payment_success'),
]