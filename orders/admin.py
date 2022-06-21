from django.contrib import admin
from orders.models import Orders, OrderItems


admin.site.register(Orders)
admin.site.register(OrderItems)
