from django.contrib import admin
from brakeless_bike.models import *

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
