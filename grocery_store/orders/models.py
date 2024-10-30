from django.db import models


# Create your models here.
class UOM(models.Model):
    uom_id = models.AutoField(primary_key=True)
    uom_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'uom'  # Name of the uom table


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    total = models.FloatField()
    datetime = models.DateTimeField()  # Consider using DateTimeField if the format allows

    class Meta:
        db_table = 'orders'  # Name of the orders table


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    uom_id = models.ForeignKey(UOM, on_delete=models.RESTRICT, db_column='uom_id', related_name='products')
    price_per_unit = models.FloatField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'  # Name of the products table


class OrderDetails(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Orders, on_delete=models.RESTRICT, db_column='order_id',
                                 related_name='order_details')
    product_id = models.ForeignKey(Products, on_delete=models.RESTRICT, db_column='product_id',
                                   related_name='order_details')
    quantity = models.FloatField()
    total_price = models.FloatField()

    class Meta:
        db_table = 'order_details'  # Name of the order_details table
        unique_together = (
            'order_id', 'product_id')  # Optional: if you want to prevent duplicates of order-product pairs