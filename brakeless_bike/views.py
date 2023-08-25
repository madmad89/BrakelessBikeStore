from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView

from .forms import CheckoutForm
from .models import Product, Category, Cart, CartItem
from django.shortcuts import render, redirect, get_object_or_404


def home_page(request):
    products = Product.objects.filter(special_price__isnull=False)
    content = {
        'products': products,
    }
    return render(request, 'home_page.html', content)


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


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


def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)  # Replace with your cart retrieval logic
    product = Product.objects.get(id=product_id)  # Replace with your product retrieval logic

    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()

    return redirect('open_cart')  # Redirect back to the cart page


def update_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)  # Replace with your cart retrieval logic
    product = Product.objects.get(id=product_id)  # Replace with your product retrieval logic

    cart_item = CartItem.objects.get(cart=cart, product=product)
    new_quantity = int(request.POST['quantity'])
    cart_item.quantity = new_quantity
    cart_item.save()

    return redirect('open_cart')


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():

            return redirect('home_page')
    else:
        form = CheckoutForm()

    context = {
        'form': form,
    }
    return render(request, 'checkout.html', context)
