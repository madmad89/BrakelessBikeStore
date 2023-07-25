from django.views.generic import DetailView

from .models import Bicycle
from django.shortcuts import render


def home_page(request):
    bicyles = Bicycle.objects.filter(special_price__isnull=False)
    return render(request, 'home_page.html', {'bicycles': bicyles})


def bicycle_list(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycle_list.html', {'bicycles': bicycles})


class BicycleDetailsView(DetailView):
    templates_name = "details_bicycle.html"
    model = Bicycle
    permission_required = 'view_bicycle'
