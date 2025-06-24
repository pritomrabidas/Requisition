from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('cart_view')

    total = sum(item.total_price() for item in cart_items)

    order = Order.objects.create(user=request.user, total_price=total)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
        # Optional: reduce stock
        item.product.quantity -= item.quantity
        item.product.save()

    cart_items.delete()  # Clear cart

    messages.success(request, f"✅ Order #{order.id} placed successfully!")
    return redirect('order_detail', order_id=order.id)

@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
