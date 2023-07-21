from django.urls import path
from . import views

urlpatterns = [
    path('', views.bicycle_list, name='bicycle_list'),
    path('', views.add_special_price, name='add_special_price'),
]