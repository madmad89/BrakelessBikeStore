from django.views.generic import DetailView

from .models import Bicycle, BikeComponents
from django.shortcuts import render


def home_page(request):
    bicycles = Bicycle.objects.filter(special_price__isnull=False)
    return render(request, 'home_page.html', {'bicycles': bicycles})


def bicycle_list(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycle_list.html', {'bicycles': bicycles})


def bicycle_components_list(request):
    components = BikeComponents.objects.all()
    return render(request, 'bicycle_components_list.html', {'components': components})


class BicycleDetailsView(DetailView):
    templates_name = "bicycle_details.html"
    model = Bicycle
    permission_required = 'view_bicycle'
