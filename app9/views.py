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
from .models import Product,CartItem
from django.contrib.auth.decorators import login_required

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
# def shop(request):
#     return render(request,'shop.html')
# # def detail(request):
#     return render(request,'detail.html')
def shop(request):
    """
    View to display all products in the shop.
    """
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})


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


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)  # Filter cart items for the logged-in user
    total_quantity = sum(item.quantity for item in cart_items)
    total_price = sum(item.total() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price})
from django.contrib import messages

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity.isdigit() and int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
    return redirect('cart')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

@login_required
def profile(request):
    user = request.user
    form = PasswordChangeForm(user)

    if request.method == 'POST':
        if 'update_email' in request.POST:
            new_email = request.POST.get('email')
            if User.objects.filter(email=new_email).exclude(username=user.username).exists():
                messages.error(request, 'Email address is already in use.')
            else:
                user.email = new_email
                user.save()
                messages.success(request, 'Email updated successfully!')
        elif 'update_password' in request.POST:
            form = PasswordChangeForm(user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Keeps the user logged in after password change
                messages.success(request, 'Password updated successfully!')
            else:
                messages.error(request, 'Please correct the error below.')

    context = {
        'user': user,
        'password_form': form,
    }
    return render(request, 'profile.html', context)