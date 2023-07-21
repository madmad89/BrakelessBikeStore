from django.contrib import admin
from brakeless_bike.models import Category, Bicycle, SpecialPrice

# Register your models here.


admin.site.register(Category)
admin.site.register(Bicycle)
admin.site.register(SpecialPrice)
