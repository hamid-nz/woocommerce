from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.

class BrandInfo(models.Model):
    brand_name= models.CharField(max_length=100, blank=True)
    site_title= models.CharField(max_length=100, blank=True)
    site_discription= models.CharField(max_length=300, blank=True)
    site_logo= models.ImageField(upload_to='images', blank=True)

class Category(models.Model):
    name= models.CharField(max_length= 100)
    category_url= AutoSlugField(populate_from= 'name', unique= True)
    discription= models.TextField(blank=True)
    category_image= models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name

AVAILABILITY_CHOICES= {
    'In Stock': 'in_stock',
    'Limited': 'limited',
    'On Order': 'on_order',
    'Out of Stock': 'out_of_stock',
}

class Product(models.Model):
    title= models.CharField(max_length=100)
    product_url= AutoSlugField(populate_from= 'title', unique= True )
    price= models.FloatField()
    actual_price= models.FloatField(blank=True)
    dicription= models.TextField(blank=True)
    delivery= models.IntegerField()
    #from=models.CharField(max_length=200 , blank=True)
    availability= models.CharField(choices=AVAILABILITY_CHOICES, max_length= 20 )
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image= models.ImageField(upload_to='product')
    product_image_2= models.ImageField(upload_to='product', blank=True)
    product_image_3= models.ImageField(upload_to='product', blank=True)
    product_image_4= models.ImageField(upload_to='product', blank=True)

    def __str__(self):
        return self.title
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



    