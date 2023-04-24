from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from account_module.models import User
from django.utils.crypto import get_random_string

from account_module.forms import Registerform, loginform


class RegisterView(View):
    def get(self, request):
        register_form = Registerform()
        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = Registerform(request.POST)

        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__exact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری میباشد')
            else:
                new_user = User(email=user_email, email_active_code=get_random_string(72), is_active=False)
                new_user.set_password(user_password)
                new_user.save()
                from django.urls import reverse
                return redirect(reverse('login_view'))

        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = loginform()
        context = {'login_form': login_form}
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        pass


class ActiveAccountView(View):
    def get(self, request, mail_activ_code):
        user: User = User.objects.filter(email_active_code__iexact=mail_activ_code).first()
        if user is not None:
            if not user.is_active :
                user.is_active = True
                user.email_active_code=get_random_string(72)
                user.save()
                return redirect(reverse('login_view'))
            else:
                pass
        raise Http404
