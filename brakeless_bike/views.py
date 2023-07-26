from django.views.generic import DetailView

from .models import Bicycle, BikeComponents, RiderApparel
from django.shortcuts import render


def home_page(request):
    bicycles = Bicycle.objects.filter(special_price__isnull=False)
    components = BikeComponents.objects.filter(special_price__isnull=False)
    apparel = RiderApparel.objects.filter(special_price__isnull=False)
    content = {
        'bicycles': bicycles,
        'components': components,
        'apparel': apparel
    }
    return render(request, 'home_page.html', content)


def bicycle_list(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycle_list.html', {'bicycles': bicycles})


def bicycle_components_list(request):
    components = BikeComponents.objects.all()
    return render(request, 'bicycle_components_list.html', {'components': components})


def rider_apparel_list(request):
    apparel = RiderApparel.objects.all()
    return render(request, 'bicycle_components_list.html', {'apparel': apparel})


class BicycleDetailsView(DetailView):
    templates_name = "bicycle_details.html"
    model = Bicycle
    permission_required = 'view_bicycle'
