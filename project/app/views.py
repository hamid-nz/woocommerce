from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, redirect
from .models import *
from django.views.generic import(
    View,
    TemplateView,
    CreateView, 
    ListView,
    UpdateView,
    DeleteView,
    DetailView
    )

class Home(TemplateView):
    template_name = 'app/index.html'

class contact(TemplateView):
    template_name = 'app/contact.html'


class ProductsView(TemplateView):
    model = Product
    template_name = 'app/products.html'
    
    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})


class SingleProductView(DetailView):
    model= Product
    template_name= 'app/single_product.html'
    context_object_name = 'product'

    def get(self, request, product_url):
        product = get_object_or_404(Product, product_url= product_url)
        return render(request, self.template_name, {'product': product})
    

class CategoryView(TemplateView):
    model = Category
    template_name = 'app/categorys.html'
    # context_object_name = 'categorys'

    def get(self, request):
        categorys = Category.objects.all()
        return render(request, self.template_name, {'categorys': categorys})


class SingleCategoryView(DetailView):
    model= Category
    template_name= 'app/single_category.html'
    context_object_name = 'category'

    def get(self, request, category_url):
        category = get_object_or_404(Category, category_url= category_url)
        return render(request, self.template_name, {'category': category})
        