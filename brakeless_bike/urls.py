from django.urls import path
from . import views

urlpatterns = [
    path('', views.bicycle_list, name='bicycle_list'),
    path('', views.home_page, name='home_page'),
]
