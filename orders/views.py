from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from store.models import *
from django.contrib.auth.models import User
from carts.models import Carts, CartItem
from django.contrib.auth.decorators import login_required
from orders.models import Orders, OrderItems

from carts.views import get_set_cart_id

def placedOrdersItems(request, order_id):

    order = Orders.objects.get(order_id=order_id)
    orderItems = OrderItems.objects.filter(order = order)

    context = {

        'orderItems': orderItems,

    }

    return render(request, 'orders/placed-orders-items.html', context)

def placedOrders(request):

    user = User.objects.get(username = request.user.username)
    orders = Orders.objects.filter(user = user)

    completeOrderItems = []

    for order in orders:
        orderItems = OrderItems.objects.filter(order = order)
        temp = []
        for orderItem in orderItems:
            
            temp.append([
                orderItem.order_id,
                orderItem.product.product_name, 
                orderItem.seller.user.username, 
                orderItem.order_item_status
                ])

        completeOrderItems.append(temp)


    

    context = {

        'orders': orders

    }
    templateUrl = 'orders/placed-orders.html'
    return render(request, templateUrl, context)

@login_required
def orderering(request):

    user = User.objects.get(username = request.user.username)
    orders_user_flag = Orders.objects.filter(user = user).exists()

    if orders_user_flag:
        orders = Orders.objects.filter(user = user).order_by('-order_id')
        print(orders[0].order_number)
        order_number = orders[0].order_number + 1
        print(order_number)
    else:
        cart = get_set_cart_id(request)
        order_number = 1
    
    print('ORDERNUMBER' + '' + str(order_number))

    orders = Orders()
    order_ide = user.username + 'aa' + str(order_number)  
    order_status = "Pending"

    orders.order_number = order_number
    orders.order_id = order_ide
    orders.user = user
    orders.order_status = order_status
    orders.save()
    # orders.user = user
    
    orderingItems(request, orders, user)

    return HttpResponse("Order Updated")

def orderingItems(request, orders, user):

    
    carts = Carts.objects.get(cart_id = get_set_cart_id(request))
    cart_items = CartItem.objects.filter(cart = carts).all()

    for cart_item in cart_items:
        orderItems = OrderItems()
        orderItems.order = orders
        orderItems.order_item_status = "Pending"
        orderItems.product = cart_item.product
        print(cart_item.product)

        prod = Product.objects.get(product_name = cart_item.product.product_name)
        
        userSeller = User.objects.get(username = prod.seller.user.username)

        productSeller = Seller.objects.get(user = userSeller)

        orderItems.seller = productSeller
        orderItems.save()

        print(orderItems.seller)




