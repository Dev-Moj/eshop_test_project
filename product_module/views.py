from django.shortcuts import render, get_object_or_404
from .models import Product


def itesm(request):
    products = Product.objects.all().order_by('price')[:3]

    return render(request, 'product_module/list_items.html', {
        'products': products
    })


def detile_items(request, slug):
    # product_item = product.objects.get(id=product_id)

    product = get_object_or_404(Product, slug=slug)

    return render(request, 'product_module/detile_item.html', {'product': product})



