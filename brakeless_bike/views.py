from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView

from .models import Product, Category, Cart, CartItem
from django.shortcuts import render, redirect, get_object_or_404


def home_page(request):
    products = Product.objects.filter(special_price__isnull=False)
    # components = BikeComponents.objects.filter(special_price__isnull=False)
    # apparel = RiderApparel.objects.filter(special_price__isnull=False)
    content = {
        'products': products,
        # 'components': components,
        # 'apparel': apparel
    }
    return render(request, 'home_page.html', content)


# class ProductListView(ListView):
#     model = Product
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


# class BicycleDetailsView(DetailView):
#     template_name = "product_details.html"
#     model = Product
#     permission_required = 'view_bicycle'

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)


class CategoryDetailsView(DetailView):
    template_name = "product_list.html"
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context[self.context_object_name]
        products = Product.objects.filter(category=category)
        context['products'] = products
        return context
    # permission_required = 'view_bicycle'


@login_required
def add_product_to_cart(request):
    if request.method == 'POST':
        open_cart, created = Cart.objects.get_or_create(user=request.user, status='open')
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart_item, created = CartItem.objects.get_or_create(product_id=product_id, cart=open_cart)
        cart_item.quantity += quantity
        cart_item.save()
    return redirect(request.META['HTTP_REFERER'])


def open_cart_view(request):
    open_cart, created = Cart.objects.get_or_create(user=request.user, status='open')
    return render(request, 'open_cart.html', {'cart': open_cart})
