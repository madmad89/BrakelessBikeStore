from django.shortcuts import render

# Create your views here.

from .models import Bicycle
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SpecialPriceForm


def bicycle_list(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycle_list.html', {'bicycles': bicycles})


def home_page(request):
    return render(request, 'home_page.html',)


def add_special_price(request, product_id):
    product = get_object_or_404(Bicycle, id=product_id)

    if request.method == 'POST':
        form = SpecialPriceForm(request.POST)
        if form.is_valid():
            special_price = form.cleaned_data['special_price']
            product.special_price = special_price
            product.save()
            return redirect('home')

    else:
        form = SpecialPriceForm()

    return render(request, 'add_special_price.html', {'form': form, 'product': product})
