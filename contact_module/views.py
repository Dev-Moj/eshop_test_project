from django.shortcuts import render, redirect
from django.views import View
from .forms import contactUsforms, contactUsModelForms
from django.views.generic.edit import FormView, CreateView
from .models import contactUs


class contactUsViews(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = contactUsModelForms
    success_url = '/contact-us'
    #
    # def form_valid(self, form):
    #     form.save()
    #     super().form_valid(form)

    # def post(self, request):
    #     contact_form = contactUsModelForms(request.POST)
    #     if contact_form.is_valid():
    #         print(contact_form.cleaned_data)
    #         contact_form.save()
    #         print(contact_form.cleaned_data)
    #         return redirect('home_page')
    #     return render(request, 'contact_module/contact_us_page.html', {
    #         'contact_forms': contact_form})
# def contact_us_page(request):
#     if request.method == 'POST':
#         contact_form = contactUsModelForms(request.POST)
#         if contact_form.is_valid():
#             print(contact_form.cleaned_data)
#             contact_form.save()
#             print(contact_form.cleaned_data)
#             return redirect('home_page')
#     else:
#         contact_form = contactUsModelForms()
#    return render(request, 'contact_module/contact_us_page.html', {'contact_forms': contact_form})
