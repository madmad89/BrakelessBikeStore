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



