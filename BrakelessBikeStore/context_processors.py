from brakeless_bike.models import Category


def navbar_data(request):
    return {'categories':Category.objects.filter(parent_category=None)}