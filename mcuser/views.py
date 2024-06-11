from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse

from mcuser.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались и вошли в аккаунт!')
            return HttpResponseRedirect(reverse('mcshop:home'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form
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
                messages.success(request, 'Вы успешно вошли в аккаунт!')

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('mcuser:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('mcshop:home'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'mcuser/login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Вы вышли из аккаунта!')
    return redirect(reverse('mcshop:home'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mcuser:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Личный кабинет',
        'form': form
    }
    return render(request, 'mcuser/profile.html', context)


def payment_delivery_info(request):
    context = {
        'title': 'Информация об оплате и доставке',
    }
    return render(request, 'mcuser/payment_delivery_info.html', context)


def support(request):
    context = {
        'title': 'Поддержка',
    }
    return render(request, 'mcuser/support.html', context)


def public_offer(request):
    context = {
        'title': 'Условия публичной оферты',
    }
    return render(request, 'mcuser/public_offer.html', context)
