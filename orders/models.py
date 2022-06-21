from tabnanny import verbose
from django.db import models
from carts.models import *
from django.contrib.auth.models import User
from seller.models import *

PENDING = "Pending"
CONFIRMED = "Confirmed"
SHIPPED = "Shipped"
DELIVERED = "Delivered"
OUT_FOR_DELIVERY = "Out for Delivery"

ORDER_STATUS_CHOICES = (
    (PENDING, "Pending"),
    (CONFIRMED, "Confirmed"),
    (SHIPPED, "Shipped"),
    (DELIVERED, "Delivered"),
    (OUT_FOR_DELIVERY, "Out for Deliver"),
)

class Orders(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.IntegerField(default=1)
    order_id = models.CharField(max_length=255, unique=True)
    order_status = models.CharField(max_length=100, default=PENDING ,choices=ORDER_STATUS_CHOICES)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self) ->str:
        return self.order_id + ' '  + self.order_status
    

class OrderItems(models.Model):

    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    order_item_status = models.CharField(max_length=255, default=PENDING, choices=ORDER_STATUS_CHOICES)

    class Meta:
        verbose_name_plural = 'Order Items'

    def __str__(self) -> str:
        return self.order.order_id + ' ' + self.product.product_name + ' ' + self.order.order_item_status