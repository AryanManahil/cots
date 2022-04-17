from django.db import models

class Product(models.Model):
    order_no = models.CharField(max_length=100)
    buyer_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_image = models.CharField(max_length=2083)
    order_qty = models.IntegerField()
    shipment_date = models.DateTimeField()

