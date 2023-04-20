from django.shortcuts import render, redirect
from django.views import View
from .forms import contactUsforms, contactUsModelForms
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView
from .models import contactUs , userprofile


class contactUsViews(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = contactUsModelForms
    success_url = '/contact-us'
    #
    # def form_valid(self, form):
    #     form.save()
    #     super().form_valid(form)


class CeateProfailView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = userprofile
    fields = '__all__'
    success_url = '/contact-us/creat-profile/'


class profilesview(ListView):
    template_name = 'contact_module/profile_list_view.html'
    model = userprofile
    context_object_name = 'profiles'

    # def post(self, request):
    #     submitted_form = profileform(request.POST,request.FILES)
    #     if submitted_form.is_valid():
    #         profile = userprofile(image=request.FILES['user_image'])
    #         profile.save()
    #
    #     return redirect('CeateProfail')
    #
    # def get(self, request):
    #     form = profileform()
    #     return render(request, 'contact_module/create_profile_page.html', {'form': form})
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
#   return render(request, 'contact_module/contact_us_page.html', {'contact_forms': contact_form})
