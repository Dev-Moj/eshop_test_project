from django.shortcuts import render, get_object_or_404
from .models import product
from django.db.models import Avg


def index(request):
    products = product.objects.all()
    total_number_of_producs = products.count()
    avg = products.aggregate(Avg('rating'))

    return render(request, 'product_module/index.html', {
        'products': products,
        'total_number_of_producs': total_number_of_producs,
        'avg': avg
    })


def itesm(request, slug):
    # product_item = product.objects.get(id=product_id)

    product_item = get_object_or_404(product, slug=slug)

    return render(request, 'product_module/list_items.html', {'item': product_item})
