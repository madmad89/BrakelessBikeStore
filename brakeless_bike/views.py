from django.views.generic import DetailView, ListView

from .models import Product
from django.shortcuts import render


def home_page(request):
    bicycles = Product.objects.filter(special_price__isnull=False)
    # components = BikeComponents.objects.filter(special_price__isnull=False)
    # apparel = RiderApparel.objects.filter(special_price__isnull=False)
    content = {
        'bicycles': bicycles,
        # 'components': components,
        # 'apparel': apparel
    }
    return render(request, 'home_page.html', content)


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# TODO  o classa care sa mosteneasca un datail view pentru toate categoriile
def bicycle_list(request):
    bicycles = Product.objects.all()
    return render(request, 'bicycle_list.html', {'bicycles': bicycles})


# def bicycle_components_list(request):
#     components = BikeComponents.objects.all()
#     return render(request, 'bicycle_components_list.html', {'components': components})


# def rider_apparel_list(request):
#     apparel = RiderApparel.objects.all()
#     return render(request, 'rider_apparel_list.html', {'apparel': apparel})


class BicycleDetailsView(DetailView):
    templates_name = "bicycle_details.html"
    model = Product
    permission_required = 'view_bicycle'
