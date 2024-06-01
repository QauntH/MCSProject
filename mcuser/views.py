from django.shortcuts import render


def register(request):
    # Ваш код для регистрации пользователя
    return render(request, 'mcuser/register.html', {})


def login(request):
    # Ваш код для входа пользователя
    return render(request, 'mcuser/login.html', {})


def profile(request):
    # Ваш код для отображения профиля пользователя
    return render(request, 'mcuser/profile.html', {})


def order_history(request):
    # Ваш код для отображения истории заказов пользователя
    return render(request, 'mcuser/order_history.html', {})
