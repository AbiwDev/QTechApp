from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from .models import Product


class ListProducts(View):
    def get(self, request):
        products = Product.objects.all().order_by("-id")

        query = request.GET.get("q")
        if query:
            products = products.filter(name__icontains=query)

        paginator = Paginator(products, 4)  # 👈 HAR SAHIFADA 3 TA
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "products/list_products.html",
            {
                "page_obj": page_obj,
                "query": query,
            }
        )
        

class DetailProduct(View):
    def get(self,request,id):
        product = get_object_or_404(Product,id=id)
        
        return render(request, "products/detail_product.html", {"product": product})
        
