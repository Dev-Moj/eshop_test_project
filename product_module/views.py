from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    products = Product.objects.all().order_by('price')[:3]

    return render(request, 'product_module/index.html', {
        'products': products
    })


def itesm(request, slug):
    # product_item = product.objects.get(id=product_id)

    product_item = get_object_or_404(Product, slug=slug)

    return render(request, 'product_module/list_items.html', {'item': product_item})


def test(request):
    return render(request, 'product_module/list_items.html')
