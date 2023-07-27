from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('bikes/', views.bicycle_list, name='bicycle_list'),
    path('bike_details/', views.BicycleDetailsView.as_view, name='bicycle_details'),
    # path('bike_components/', views.bicycle_components_list, name='bicycle_components'),
    # path('biker_apparel/', views.rider_apparel_list, name='biker_apparel'),

]
