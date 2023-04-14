from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('test', views.test)
    # path('<slug:slug>', views.itesm, name='item_list')

]
