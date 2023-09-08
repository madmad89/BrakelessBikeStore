from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('open-cart/', views.open_cart_view, name='open_cart'),
    path('add-product-to-cart/', views.add_product_to_cart, name='add_product_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('category/<int:pk>/', views.CategoryDetailsView.as_view(), name='category_details'),
    path('search/', views.search_products, name='search_products'),

]
