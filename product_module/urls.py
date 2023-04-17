from django.urls import path
from . import views

urlpatterns = [
    path('', views.listItemsView.as_view()),
    path('<slug:slug>', views.detile_items, name='detile_items')

]
