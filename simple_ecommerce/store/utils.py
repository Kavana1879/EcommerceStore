import json
from .models import *

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # Get cart from session
        try:
            cart = request.session.get('cart', {})
        except:
            cart = {}
            
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

        for i in cart:
            # We use try block to prevent items in session cart that may have been removed from database
            try:
                if cart[i]['quantity'] > 0:
                    cartItems += cart[i]['quantity']

                    product = Product.objects.get(id=i)
                    total = (product.price * cart[i]['quantity'])

                    order['get_cart_total'] += total
                    order['get_cart_items'] += cart[i]['quantity']

                    item = {
                        'id': product.id,
                        'product': {
                            'id': product.id,
                            'name': product.name,
                            'price': product.price,
                            'image': product.image,
                        },
                        'quantity': cart[i]['quantity'],
                        'get_total': total,
                    }
                    items.append(item)
            except:
                pass
            
    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(request, data):
    # If we need to process checkout for guest, we can do it here.
    # Currently the requirement is to prompt login.
    pass
