from django.shortcuts import render


def checkout(request):
    context = {
        'title': 'Интернет-магазин компьютеров - Оформление заказа',
    }
    return render(request, 'mcorders/checkout.html', context)
