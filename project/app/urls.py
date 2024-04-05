from django.urls import path
from .views import *
# Create your views here.

urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('product/', ProductsView.as_view(), name='products'),
    path('product/<slug:product_url>', SingleProductView.as_view(), name='single_product'),
    path('category/', CategoryView.as_view(), name='categorys'),
    path('category/<slug:category_url>', SingleCategoryView.as_view(), name='single_category'),

#simple pages
    path('contact/', contact.as_view(), name='contact'),
]
