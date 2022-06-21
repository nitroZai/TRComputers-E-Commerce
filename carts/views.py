from django.shortcuts import redirect, render
from carts.models import Carts, CartItem
from store.models import Product

def get_set_cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def cart(request, total = 0, quantity = 0, cart_items = None):

    tax = 0
    grand_total = 0

    try:
        cart = Carts.objects.get(cart_id = get_set_cart_id(request))
        cart_items = CartItem.objects.filter(
            cart = cart, is_active = True
        )

        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity
        
        tax = (18*total)/100
        grand_total = total + tax
    except Carts.DoesNotExist:
        pass

    context  = {
        'tax': tax,
        'grand_total': grand_total,
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items
    }

    return render(request, 'store/cart.html', context)

def add_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    print(product.product_name)

    try:
        cart = Carts.objects.get(cart_id = get_set_cart_id(request))
    except Carts.DoesNotExist:
        cart = Carts()
        cart.cart_id = get_set_cart_id(request)
        cart.save()

    cart_item_flag = CartItem.objects.filter(cart = cart, product = product).exists()
    cart_item = CartItem()

    if cart_item_flag:
        cart_item = CartItem.objects.filter(product = product, cart = cart)
        quantity = cart_item[0].quantity + 1
        cart_item.update(quantity=quantity)
        
    else:

        cart_item.product = product
        cart_item.cart = cart
        cart_item.quantity = 1
        cart_item.save()

    return redirect('cart')

def remove_cart_button(request, product_id):

    product = Product.objects.get(id = product_id)
    cart = Carts.objects.get(cart_id = get_set_cart_id(request))
    cart_item = CartItem.objects.filter(product = product, cart = cart)

    if cart_item[0].quantity > 1:

        quantity = cart_item[0].quantity - 1
        cart_item.update(quantity = quantity)

    else:

        cart_item.delete()

    return redirect('cart')

def remove_cart_item(request, product_id):

    cart = Carts.objects.get(cart_id = get_set_cart_id(request))
    product = Product.objects.get(id = product_id)

    cart_item = CartItem.objects.filter(cart = cart, product = product)
    cart_item.delete()

    return redirect('cart')


# def plus_cart_item(request, product_id):

#     cart = Carts.objects.get(cart_id = get_set_cart_id(request))
#     product = Product.objects.get(
#         id = product_id
#     )

#     cart_item = CartItem.objects.filter(
#         product = product,
#         cart = cart
#     )

#     quantity = cart_item[0].quantity + 1

#     cart_item.update(quantity = quantity)

#     return redirect('cart')

# def minus_cart_item(request, product_id):
#     cart = Carts.objects.get(cart_id = get_set_cart_id(request))
#     product = Product.objects.get(
#         id = product_id
#     )

#     cart_item = CartItem.objects.filter(
#         product = product,
#         cart = cart
#     )

#     tempBool = False
#     if cart_item[0].quantity == 1:
#         tempBool = True
#         redirect('cart')
    
#     quantity = cart_item[0].quantity - 1

#     cart_item.update(quantity = quantity)

#     return redirect('cart')
