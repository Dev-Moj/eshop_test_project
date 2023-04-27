from django.shortcuts import render
from django.views.generic import TemplateView


class homeView(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = 'this is date'
        return context


def content_page(request):
    return render(request, 'home_module/contact_page.html')


def site_heder_component(request):
    return render(request, 'shared/sitt_heder_component.html')


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')
