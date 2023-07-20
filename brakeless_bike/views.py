from django.shortcuts import render

# Create your views here.

from .models import Bicycle


def bicycle_list(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycle_list.html', {'bicycles': bicycles})
