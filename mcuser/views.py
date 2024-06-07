from django.shortcuts import render


def register(request):
    return render(request, 'mcuser/register.html')


def login(request):
    return render(request, 'mcuser/login.html')


def profile(request):
    return render(request, 'mcuser/profile.html')


def payment_delivery_info(request):
    return render(request, 'mcuser/payment_delivery_info.html')


def support(request):
    return render(request, 'mcuser/support.html')


def public_offer(request):
    return render(request, 'mcuser/public_offer.html')
