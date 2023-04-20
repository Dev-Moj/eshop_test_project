from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUsViews.as_view(), name='contactUs'),
    path('creat-profile/', views.CeateProfailView.as_view(), name='CeateProfail'),
    path('profile/', views.profilesview.as_view(), name='Profail')
]
