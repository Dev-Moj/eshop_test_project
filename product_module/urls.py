from django.urls import path
from . import views

urlpatterns = [
    path('', views.itesm),
    path('<slug:slug>', views.detile_items, name='detile_items')

]
