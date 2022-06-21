from django.db import models
from django.urls import reverse
from seller.models import Seller

class Category(models.Model):

    category_name = models.CharField(max_length=255, unique=True)
    category_slug = models.SlugField(max_length=255, unique=True)
    
    class Meta: 
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.category_name

    def get_url(self) -> str:
        return reverse('products_by_category', args=[self.category_slug])


class Product(models.Model):

    product_name = models.CharField(max_length=255, unique=True)
    product_slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=255, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.product_name

    def get_url(self) -> str:
        return reverse('product_detail', args=[self.category.category_slug, self.product_slug])
