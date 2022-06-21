from django.shortcuts import get_object_or_404, render
from .models import Product, Category
from django.db.models import Q

def search(request):

    product_count = 0

    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')

        if keyword:

            products = Product.objects.filter(
                Q(
                    description__icontains = keyword
                ) | Q(
                    product_name__icontains = keyword
                )
            )

            product_count = products.count()

    context = {
        'products': products,
        'products_count': product_count
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):

    category = Category.objects.get(category_slug=category_slug)

    single_product = Product.objects.get(
        category = category,
        product_slug = product_slug,
    )

    pass

    context =  {'single_product': single_product,}

    return render(request, 'store/product_detail.html', context )

def store(request, category_slug=None):

    categories = None
    products = None

    if category_slug == None:

        products = Product.objects.all().filter(is_available = True).order_by('id')

        products_count = products.count()

    else:

        categories = get_object_or_404(Category, category_slug=category_slug)
        products = Product.objects.filter(category = categories, is_available = True)

        products_count = products.count()


    context = {

        'products': products,
        'products_count': products_count

    }

    return render(request, 'store/store.html', context)


