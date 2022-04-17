from django.contrib import admin
from .models import  Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('order_no','buyer_name','product_name','order_qty','shipment_date')

admin.site.register(Product,ProductAdmin)
# Register your models here.
