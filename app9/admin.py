from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product,CartItem,BillingDetails,Order,OrderItem
# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(BillingDetails)

admin.site.register(Order)

admin.site.register(OrderItem)