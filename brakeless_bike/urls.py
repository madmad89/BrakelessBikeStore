from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('bikes/', views.product_list, name='product_list'),
    path('bike_details/', views.BicycleDetailsView.as_view(), name='bicycle_details'),
    path('open-cart/', views.open_cart_view, name='open_cart'),
    path('add-product-to-cart/', views.add_product_to_cart, name='add_product_to_cart'),
    path('category/<int:pk>/', views.CategoryDetailsView.as_view(), name='category_details'),

]
