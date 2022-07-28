from django.shortcuts import render
from .forms import CreateOrderFrom
from .models import OrderItem
from cart.cart import Cart

def create_order(request):
    cart = Cart(request)
    if request.method == "POST":
        form = CreateOrderFrom(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], count=item['count'])
            cart.clear()
            return render(request, 'created.html', {'order': order})
    else:
        form = CreateOrderFrom()
        return render(request, 'create_order.html', context={'cart': cart, 'form': form})
