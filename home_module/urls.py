from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView.as_view(), name='home_page'),
    path('content', views.content_page),

]