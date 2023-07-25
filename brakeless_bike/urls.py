from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('bikes/', views.bicycle_list, name='bicycle_list'),
    path('bicycle_components/', views.BicycleDetailsView.as_view, name='bicycle_components'),

]
