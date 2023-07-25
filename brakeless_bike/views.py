
from .models import Bicycle
from django.shortcuts import render


def bicycle_list(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycle_list.html', {'bicycles': bicycles})


def home_page(request):
    bicyles = Bicycle.objects.filter(special_price__isnull=False)
    return render(request, 'home_page.html', {'bicycles': bicyles})



