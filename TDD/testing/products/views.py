from django.shortcuts import render
from django.shortcuts import get_object_or_404

from products.models import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, kwargs={'pk': pk})
    return render(request, 'products/product_detail.html', {'product': product})

