from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from account_module.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout

from account_module.forms import Registerform, loginform, ForgotPassword_form, ResetPassword_form


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
                new_user = User(email=user_email, email_active_code=get_random_string(72), is_active=False,
                                username=user_email)
                new_user.set_password(user_password)
                new_user.save()

                return redirect(reverse('home_page'))

        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = loginform()
        context = {'login_form': login_form}
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = loginform(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if not user.is_active:
                print('=================+==================')
                login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
            else:
                if user is not None:
                    is_password_corrct = user.check_password(user_pass)
                    if is_password_corrct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'حساب کاربری با مشخصات وارد شده یافت نشد')


                else:
                    login_form.add_error('email', 'حساب کاربری با مشخصات وارد شده یافت نشد')
        context = {'login_form': login_form}
        return render(request, 'account_module/login.html', context)


class ActiveAccountView(View):
    def get(self, request, mail_activ_code):
        user: User = User.objects.filter(email_active_code__iexact=mail_activ_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login_view'))
            else:
                pass
        raise Http404


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forgotpassword_form = ForgotPassword_form()
        context = {'forgotPassword_form': forgotpassword_form}
        return render(request, 'account_module/forgot_password.html', context)

    def post(self, request: HttpRequest):
        forgotpassword_form = ForgotPassword_form(request.POST)
        if forgotpassword_form.is_valid():
            user_email = forgotpassword_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                pass
        context = {'forgotPassword_form': forgotpassword_form}
        return render(request, 'account_module/forgot_password.html', context)


class reset_passView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_view'))
        resetpassword_form = ResetPassword_form()
        context = {'resetpassword_form': resetpassword_form,
                   'user': user
                   }
        return render(request, 'account_module/reset_pass.html', context)

    def post(self, request: HttpRequest, active_code):
        resetpassword_form = ResetPassword_form(request.POST)
        if resetpassword_form.is_valid():
            user: User = User.objects.filter(email_active_code__iexact=active_code).first()
            if user is None:
                return redirect(reverse('login_view'))
            user_new_pass = resetpassword_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_view'))
        resetpassword_form = ResetPassword_form()
        context = {'resetpassword_form': resetpassword_form
                   }
        return render(request, 'account_module/reset_pass.html', context)
