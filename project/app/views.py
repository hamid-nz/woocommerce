from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorys= Category.objects.all()
        context["categorys"]= categorys
        return context
    
    # def most_used_categories(request):
    #     most_used_categories = Category.objects.annotate(num_products=Count('products')).order_by('-num_products')
    #     return render(request, 'app/index.html', {'most_used_categories': most_used_categories})
    

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

    def get(self, request, product_url) :
        product = get_object_or_404(Product, product_url= product_url)
        related_product= Product.objects.filter(category= product.category).exclude(pk= product.pk)
        context={
            'product': product,
            'related_product': related_product
        }
        return render(request, self.template_name, context)

    def add_to_cart(request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
           quantity = int(request.POST.get('quantity', 1))
        # Check if item is already in the cart
           cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
           if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return render (request, 'app/single_product.html')



class CategoryView(TemplateView):
    model = Category
    template_name= 'app/categorys.html',
    def get(self, request):
        categorys = Category.objects.all()
        return render(request, self.template_name, {'categorys': categorys})
    

def get_product_by_category(request, category_url):
    cats= Category.objects.get(category_url= category_url)
    products= Product.objects.filter(category= cats)
    context= { 'products': products, 'cats':cats}
    return render(request, 'app/single_category.html', context )

 


# def remove_from_cart(request, cart_item_id):
#     cart_item = get_object_or_404(CartItem, pk=cart_item_id)
#     if request.method == 'POST':
#         cart_item.delete()
#     return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})






@login_required(login_url='sign-in')
def add_job(request):
    if (request.POST):
        title=request.POST['title']     
        company= request.POST['company']
        pay= request.POST['pay']
        job_type= request.POST['job_type']
        location= request.POST['location']
        application_deadline= request.POST['application_deadline']
        job_discription= request.POST['job_discription']
        positions= request.POST['positions']
        models.Job.objects.create(
            title= title, 
            company= company, 
            pay= pay, 
            job_type= job_type, 
            location= location, 
            application_deadline= application_deadline, 
            job_discription= job_discription,  
            positions= positions,
            )
        return render(request, 'company/jobsHome.html')    
    else:
        return render(request, 'company/add-new-job.html')
    
# user authentication Login and register
@login_required(login_url='sign-in')
def Account(request):
    return render(request,'app/account.html' )  

def sign_in(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        pass1= request.POST.get('pass1')
        user= authenticate(request, username= username, password= pass1)
        if user is not None:
            login(request, user)
            return redirect(Account)
        else:
            return HttpResponse(" <h3>Username or Password is incorrect! Try again</h3>")
    
    return render (request, 'app/sign-in.html')

def sign_up(request):
    if request.method == 'POST':
        name= request.POST.get('Name')
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('pass1')
        pass2= request.POST.get('pass2')
        if password!= pass2:
            return HttpResponse("Your password does'nt match")
        else:       
         new_user = User.objects.create_user(username, email,  password )
         new_user.save()     
         return redirect('sign-in')
    
    return render (request, 'app/sign-up.html')
    
def sign_out(request):
     logout(request)
     return redirect('sign-in')