from django.contrib import admin
from .models import  Product,Buyer,Supplier

class ProductAdmin(admin.ModelAdmin):
    list_display = ('order_no','buyer_name','product_name','order_qty','shipment_date')

class BuyerAdmin(admin.ModelAdmin):
    list_display = ('buyer_name','buyer_contact_no','buyer_email','buyer_address')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'supplier_contact_no', 'supplier_email', 'supplier_address')


admin.site.register(Product,ProductAdmin)
admin.site.register(Buyer,BuyerAdmin)
admin.site.register(Supplier,SupplierAdmin)
# Register your models here.
