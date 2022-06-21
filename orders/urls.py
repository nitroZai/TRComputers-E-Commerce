from django.urls import path
from .views import *

urlpatterns  = [

    path('ordering/', orderering, name='ordering'),
    path('placed-orders/', placedOrders, name='placedOrders'),
    path('placed_orders_items/<str:order_id>', placedOrdersItems, name='placedOrdersItems')

]