from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display= [  'title', 'price', 'product_image', 'category','availability' ]
    
admin.site.register(Category)
