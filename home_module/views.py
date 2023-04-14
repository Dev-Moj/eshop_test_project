from django.shortcuts import render


def index_page(request):
    return render(request, 'home_module/index.html')


def content_page(request):
    return render(request, 'home_module/contact_page.html')


def site_heder_component(request):
    return render(request, 'shared/sitt_heder_component.html')


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')
