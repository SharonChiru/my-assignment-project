 # sharon/urls.py
from django.urls import path
from . import views
#from .views import home, additional_page(to be deleted)


urlpatterns = [
    path('', views.home, name='home'),
    path('additional/', views.additional_page, name='additional_page'),
]
#14/12/2023
# sharon/urls.py
from django.urls import path
from .views import home, additional_page

urlpatterns = [
    path('', home, name='home'),
    path('additional/', additional_page, name='additional_page'),
]


