from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from mcuser.forms import UserLoginForm


def register(request):
    context = {
        'title': 'Регистрация',
    }
    return render(request, 'mcuser/register.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mcshop:home'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'mcuser/login.html', context)


def logout(request):
    pass


def profile(request):
    context = {
        'title': 'Личный кабинет',
    }
    return render(request, 'mcuser/profile.html', context)


def payment_delivery_info(request):
    context = {
        'title': 'Информация об оплате и доставке',
    }
    return render(request, 'mcuser/payment_delivery_info.html')


def support(request):
    context = {
        'title': 'Поддержка',
    }
    return render(request, 'mcuser/support.html')


def public_offer(request):
    return render(request, 'mcuser/public_offer.html')
