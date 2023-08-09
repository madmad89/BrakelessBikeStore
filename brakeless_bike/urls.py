from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('products/', views.product_list, name='product_list'),
    # path('product_details/', views.BicycleDetailsView.as_view(), name='product_details'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('open-cart/', views.open_cart_view, name='open_cart'),
    path('add-product-to-cart/', views.add_product_to_cart, name='add_product_to_cart'),
    path('category/<int:pk>/', views.CategoryDetailsView.as_view(), name='category_details'),

]
