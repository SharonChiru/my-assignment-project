 # sharon/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('additional/', views.additional_page, name='additional_page'),
]



