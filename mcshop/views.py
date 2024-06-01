from django.shortcuts import render

from mcshop.models import *


def base_generic(request):
    categories = Categories.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'base_generic.html', context)


def home(request):

    context = {
        'title': 'Интернет-магазин компьютеров'
    }
    return render(request, 'home.html', context)


def beta(request):
    return render(request, 'mcshop/pc_series_pages/beta.html')


def upsilon(request):
    return render(request, 'mcshop/pc_series_pages/upsilon.html')


def configurator(request):
    return render(request, 'mcshop/configurator.html')


def payment_delivery_info(request):
    return render(request, 'mcshop/payment_delivery_info.html')


def support(request):
    return render(request, 'mcshop/support.html')


def custom(request):
    return render(request, 'mcshop/pc_models_pages/custom.html')


def notebook(request):
    return render(request, 'mcshop/pc_models_pages/notebook.html')


def optimal(request):
    return render(request, 'mcshop/pc_models_pages/optimal.html')


def powerful(request):
    return render(request, 'mcshop/pc_models_pages/powerful.html')


def alpha(request):
    return render(request, 'mcshop/pc_series_pages/alpha.html')


def delta(request):
    return render(request, 'mcshop/pc_series_pages/delta.html')


def gamma(request):
    return render(request, 'mcshop/pc_series_pages/gamma.html')


def kappa(request):
    return render(request, 'mcshop/pc_series_pages/kappa.html')


def lambda_page(request):
    return render(request, 'mcshop/pc_series_pages/lambda.html')


def omega(request):
    return render(request, 'mcshop/pc_series_pages/omega.html')


def omicron(request):
    return render(request, 'mcshop/pc_series_pages/omicron.html')


def sigma(request):
    return render(request, 'mcshop/pc_series_pages/sigma.html')


def theta(request):
    return render(request, 'mcshop/pc_series_pages/theta.html')


def zeta(request):
    return render(request, 'mcshop/pc_series_pages/zeta.html')


def product_detail(request):
    return render(request, 'mcshop/product_detail.html')


def cart(request):
    return render(request, 'mcshop/cart.html', {})


def checkout(request):
    return render(request, 'mcshop/checkout.html', {})
