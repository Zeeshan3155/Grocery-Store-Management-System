from django.contrib import admin
from orders.models import Products, OrderDetails, Orders, UOM
# Register your models here.
admin.site.register(Products)
admin.site.register(OrderDetails)
admin.site.register(Orders)
admin.site.register(UOM)