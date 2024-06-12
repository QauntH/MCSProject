from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from mcshop.models import Cart

from mcorders.forms import CreateOrderForm
from mcorders.models import Order, OrderItem


@login_required
def checkout(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                            email=form.cleaned_data['email'],
                            comment=form.cleaned_data['comment'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.save()

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('mcuser:profile')
            except ValidationError:
                messages.success(request, 'Что-то пошло не так :(')
                return redirect('mcorders:checkout')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Интернет-магазин компьютеров - Оформление заказа',
        'form': form,
        'orders': True,
    }
    return render(request, 'mcorders/checkout.html', context=context)
