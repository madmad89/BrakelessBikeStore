from django.contrib import admin
from brakeless_bike.models import Category, Bicycle, BikeComponents, RiderApparel

# Register your models here.


admin.site.register(Category)
admin.site.register(Bicycle)
admin.site.register(BikeComponents)
admin.site.register(RiderApparel)
