from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display= [  'title', 'price', 'product_image', 'category','availability' ]
    
@admin.register(CartItem)
class CartModelAdmin(admin.ModelAdmin):
    list_display= [  'id', 'user', 'product', 'quantity']
    
admin.site.register(Category)
admin.site.register(BrandInfo)
