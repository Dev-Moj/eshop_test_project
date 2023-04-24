from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.views.generic import ListView

from .models import Product


# class listItemsView(TemplateView):
#     template_name = 'product_module/list_items.html'
#
#     def get_context_data(self, **kwargs):
#         products = Product.objects.all().order_by('price')[:3]
#         context = super().get_context_data(**kwargs)
#         context['products'] = products
#         return context

class listItemsView(ListView):
    template_name = 'product_module/list_items.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_queryset(self):
        base_query = super(listItemsView, self).get_queryset()
        date = base_query.filter(is_active=True)
        return date


# def list_itesms(request):
#     products = Product.objects.all().order_by('price')[:3]
#
#     return render(request, 'product_module/list_items.html', {
#         'products': products
#     })


# def detile_items(request, slug):
#     # product_item = product.objects.get(id=product_id)
#
#     product = get_object_or_404(Product, slug=slug)
#
#     return render(request, 'product_module/detile_item.html', {'product': product})
class detileItemsView(DetailView):
    template_name = 'product_module/detile_item.html'
    model = Product

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get('product-favorite')
        contex['is_favorite'] = str(loaded_product.id) == favorite_product_id
        return contex


class addproductfavorite(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['product-favorite'] = product_id
        print(product_id)
        return redirect(product.get_absolute_url())
