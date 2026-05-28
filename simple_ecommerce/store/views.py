from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json
import datetime

from .models import *
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .utils import cartData


@ensure_csrf_cookie
def home(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    # Filtering
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Sorting
    sort_by = request.GET.get('sort')
    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'newest':
        products = products.order_by('-created')

    return render(request, 'home.html', {
        'products': products,
        'categories': categories,
        'cartItems': cartItems,
    })


@ensure_csrf_cookie
def product_detail(request, slug):
    data = cartData(request)
    cartItems = data['cartItems']

    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'product_detail.html', {
        'product': product,
        'cartItems': cartItems,
    })


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    return render(request, 'cart.html', {
        'items': items,
        'order': order,
        'cartItems': cartItems
    })


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, "Please login or register to place an order.")
            return redirect('login')
            
        order_obj = Order.objects.get(id=order.id)
        order_obj.transaction_id = str(datetime.datetime.now().timestamp())
        order_obj.complete = True
        order_obj.save()
        messages.success(request, "Order placed successfully!")
        return redirect('home')

    return render(request, 'checkout.html', {
        'items': items,
        'order': order,
        'cartItems': cartItems
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        order_item.quantity += 1
        order_item.save()
    else:
        # Session cart
        cart = request.session.get('cart', {})
        prod_id = str(product_id)
        if prod_id in cart:
            cart[prod_id]['quantity'] += 1
        else:
            cart[prod_id] = {'quantity': 1}
        request.session['cart'] = cart

    messages.success(request, f"{product.name} was added to your cart.")
    return redirect('cart')


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    if request.user.is_authenticated:
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=request.user, complete=False)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            order_item.quantity += 1
        elif action == 'remove':
            order_item.quantity -= 1

        order_item.save()

        if order_item.quantity <= 0:
            order_item.delete()
    else:
        # Session cart update
        cart = request.session.get('cart', {})
        prod_id = str(productId)
        if prod_id in cart:
            if action == 'add':
                cart[prod_id]['quantity'] += 1
            elif action == 'remove':
                cart[prod_id]['quantity'] -= 1

            if cart[prod_id]['quantity'] <= 0:
                cart.pop(prod_id)
        
        request.session['cart'] = cart

    return JsonResponse("Updated", safe=False)


def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # SAFE PROFILE CREATION
            CustomerProfile.objects.get_or_create(user=user)

            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def profile(request):
    # SAFE PROFILE ACCESS (FIX CRASH)
    profile, created = CustomerProfile.objects.get_or_create(user=request.user)

    data = cartData(request)
    cartItems = data['cartItems']

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    orders = Order.objects.filter(customer=request.user, complete=True).order_by('-date_ordered')

    return render(request, 'profile.html', {
        'u_form': u_form,
        'p_form': p_form,
        'orders': orders,
        'cartItems': cartItems
    })