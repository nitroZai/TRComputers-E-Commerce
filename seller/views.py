from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from store.models import *
from store.models import Category
from orders.models import Orders, OrderItems

def dashboard(request):
    return render(request, 'seller/dashboard.html')

def orders_received(request):

    user = User.objects.get(username = request.user.username)

    seller = Seller.objects.get(user = request.user)

    # Getting the User who ordered the items

    orderItems = OrderItems.objects.filter(
        seller = seller
    )

    context = {
        'orderItems': orderItems,
    }
    

    return render(request, 'seller/orders-received.html', context)

def generate_product_slug(product_name):

    productNameArray = product_name.split(' ')
    
    productJoinVariable = '-'.join(productNameArray).lower()

    return productJoinVariable

def productUpload(request):

    if request.method == 'POST':

        product_name = request.POST.get('product_name')
        product_slug = generate_product_slug(product_name)
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        stock = request.POST.get('stock')
        category = request.POST.get('category')
        print(request.FILES.get('image'))

        fileSystemStorage = FileSystemStorage()
        image_file = fileSystemStorage.save(image.name, image)
        image_url = fileSystemStorage.url(image_file)

        categoryObject = Category.objects.get(category_name = category)
        user = User.objects.get(username = request.user.username)
        seller = Seller.objects.get(user = user)

        product = Product()
        product.product_name = product_name
        product.product_slug = product_slug
        product.description = description
        product.price = price
        product.image = image_url
        product.stock = stock
        product.category = categoryObject
        product.seller = seller
        product.save()

        return HttpResponse("Product Upload sucessfull")
    else:
        
        categories = Category.objects.all()

        context = {
            'categories': categories
        }
        return render(request,'seller/productupload.html', context)


