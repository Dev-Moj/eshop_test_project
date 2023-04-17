from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUsViews.as_view(), name='contactUs')
]
