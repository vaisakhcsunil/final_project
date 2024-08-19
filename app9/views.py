from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from.forms import SignupForm
from django.contrib.auth.hashers import make_password
from . forms import SignupForm,LoginForm,ProductForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Product
def index(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User(username=username,email=email)
            user.set_password(password)
            user.save()
            return redirect('login_page')
    else:
        form=SignupForm()
    return render(request,'index.html',{'form':form})
def shop(request):
    return render(request,'shop.html')
# def detail(request):
#     return render(request,'detail.html')



def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=form.instance.pk)
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail.html', {'product': product})

def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')

def login_page(request):
    if request.method == 'POST':       
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']   
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('shop')
            else:
                # Display an error message if authentication fails
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            # Display an error message if the form is invalid
            messages.error(request, 'Invalid form submission. Please check your input.')        
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
