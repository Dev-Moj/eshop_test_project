from django.urls import path
from . import views

urlpatterns = [
    path('', views.listItemsView.as_view()),
    path('product-favorite/', views.addproductfavorite.as_view(), name='product_favorite'),
    path('<slug:slug>', views.detileItemsView.as_view(), name='detile_items')


]
