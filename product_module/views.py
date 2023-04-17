from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Product


class listItemsView(TemplateView):
    template_name = 'product_module/list_items.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.all().order_by('price')[:3]
        context = super().get_context_data(**kwargs)
        context['products'] = products
        return context


# def list_itesms(request):
#     products = Product.objects.all().order_by('price')[:3]
#
#     return render(request, 'product_module/list_items.html', {
#         'products': products
#     })


def detile_items(request, slug):
    # product_item = product.objects.get(id=product_id)

    product = get_object_or_404(Product, slug=slug)

    return render(request, 'product_module/detile_item.html', {'product': product})
