from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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