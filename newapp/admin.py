from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(customers)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(ShippingAdress)
admin.site.register(newsletter)