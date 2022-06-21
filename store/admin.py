from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'category_slug': ('category_name',) }
    list_display = ['category_name', 'category_slug']

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'product_slug': ('product_name',) }
    list_display = (
        'product_name',
        'product_slug',
        'price',
        'stock',
        'category',
        'is_available',
        'modified_date',
    )

admin.site.register(Category, CategoryAdmin)
# Register your models here.
admin.site.register(Product, ProductAdmin)
