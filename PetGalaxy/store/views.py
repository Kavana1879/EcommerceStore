from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product, UserProfile, Address, Order, OrderItem
from .forms import UserRegistrationForm, UserLoginForm, AddressForm
from .cart import Cart

def splash(request):
    return render(request, 'splash.html')

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:8]
    return render(request, 'home.html', {'categories': categories, 'products': products})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'category.html', {'category': category, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    return render(request, 'product_detail.html', {'product': product, 'related_products': related_products})

def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'products': products, 'query': query})

def cart_detail(request):
    return render(request, 'cart.html')

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    messages.success(request, f'Added {product.name} to your cart.')
    return redirect('cart_detail')

def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        cart.add(product=product, quantity=quantity, override_quantity=True)
        messages.success(request, f'Updated {product.name} quantity.')
    else:
        cart.remove(product)
        messages.success(request, f'Removed {product.name} from cart.')
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'Removed {product.name} from your cart.')
    return redirect('cart_detail')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                phone_number=form.cleaned_data['phone_number']
            )
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'profile.html', {'profile': request.user.profile})

@login_required
def address_list(request):
    addresses = request.user.addresses.all()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, 'Address added successfully.')
            return redirect('address_list')
    else:
        form = AddressForm()
    return render(request, 'address.html', {'addresses': addresses, 'form': form})

@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart_detail')
    addresses = request.user.addresses.all()
    if request.method == 'POST':
        address_id = request.POST.get('address')
        if not address_id:
            messages.error(request, 'Please select a shipping address.')
            return redirect('checkout')
        address = get_object_or_404(Address, id=address_id, user=request.user)
        addr_str = f"{address.full_name}, {address.address_line_1}, {address.address_line_2}, {address.city}, {address.state} - {address.pincode}. Phone: {address.phone_number}"
        
        order = Order.objects.create(
            user=request.user,
            total_amount=cart.get_total_price(),
            shipping_address=addr_str
        )
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['price'],
                subtotal=item['total_price']
            )
        cart.clear()
        return redirect('order_success', order_id=order.id)
    return render(request, 'checkout.html', {'addresses': addresses})

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_success.html', {'order': order})

@login_required
def order_history(request):
    orders = request.user.orders.all().order_by('-created_at')
    return render(request, 'order_history.html', {'orders': orders})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
