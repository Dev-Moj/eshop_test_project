from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('register/', views.RegisterView.as_view(), name='register_view'),
    path('forgot-pass/', views.ForgetPasswordView.as_view(), name='forgot_pass'),
    path('reset-pass/<active_code>', views.reset_passView.as_view(), name='resetـpass_View'),
    path('activate-account/<mail_activ_code>', views.ActiveAccountView.as_view(), name='activate_account')

]
