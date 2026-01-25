from django.urls import path 
from . import views

app_name = "products"

urlpatterns = [
    path("",views.ListProducts.as_view(),name="list_products"),
    path("detail/<int:id>",views.DetailProduct.as_view(),name="detail_product"),
]