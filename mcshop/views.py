from django.shortcuts import render
from django.db.models import Q

from mcshop.models import *


def base_generic(request):
    context = {
        'title': 'Шаблон'
    }
    return render(request, 'base_generic.html', context)


def search(request):
    query = request.GET.get('q')
    if query:
        results = Products.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(graphic_card__icontains=query) |
            Q(processor__icontains=query) | Q(motherboard__icontains=query) | Q(ssd__icontains=query) |
            Q(ram__icontains=query) | Q(pc_case__icontains=query) | Q(power_unit__icontains=query)
        )
    else:
        results = Products.objects.none()

    context = {
        'title': 'Поиск по магазину',
        'results': results,
        'query': query,
    }
    # if category_slug == 'all':
    #     mcshop = Products.objects.all()
    # else:
    #     mcshop = get_object_or_404(Products.objects.filter(category_slug=category_slug))
    #
    # paginator = Paginator(mcshop, 6)
    # current_page = paginator.page(1)
    #
    # context = {
    #     'title': 'Главная - Поиск',
    #     'mcshop': current_page,
    # }

    return render(request, 'mcshop/search.html', context)


def home(request):
    products = Products.objects.all().filter(price__gt=90000).filter(price__lt=105000).order_by('price')

    context = {
        'title': 'Интернет-магазин компьютеров',
        'products': products,
    }
    return render(request, 'home.html', context)


def beta(request):
    products = Products.objects.all().filter(name__contains='Beta')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия BETA',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/beta.html', context)


def upsilon(request):
    products = Products.objects.all().filter(name__contains='Upsilon')

    context = {
        'title': 'Интернет-магазин – Серия UPSILON',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/upsilon.html', context)


def custom(request):
    sigma_series = Series.objects.get(name='Sigma')
    kappa_series = Series.objects.get(name='Kappa')
    lambda_series = Series.objects.get(name='Lambda')

    sigma_products = sigma_series.products.all()
    kappa_products = kappa_series.products.all()
    lambda_products = lambda_series.products.all()

    context = {
        'title': 'Интернет-магазин компьютеров – Категория CUSTOM',
        'sigma_series': sigma_series,
        'kappa_series': kappa_series,
        'lambda_series': lambda_series,
        'sigma_products': sigma_products,
        'kappa_products': kappa_products,
        'lambda_products': lambda_products,
    }
    return render(request, 'mcshop/pc_models_pages/custom.html', context)


def notebook(request):
    omicron_series = Series.objects.get(name='Omicron')
    zeta_series = Series.objects.get(name='Zeta')
    omega_series = Series.objects.get(name='Omega')

    omicron_products = omicron_series.products.all()
    zeta_products = zeta_series.products.all()
    omega_products = omega_series.products.all()

    context = {
        'title': 'Интернет-магазин компьютеров – Категория NOTEBOOKS',
        'omicron_series': omicron_series,
        'zeta_series': zeta_series,
        'omega_series': omega_series,
        'omicron_products': omicron_products,
        'zeta_products': zeta_products,
        'omega_products': omega_products,
    }
    return render(request, 'mcshop/pc_models_pages/notebook.html', context)


def optimal(request):
    beta_series = Series.objects.get(name='Beta')
    theta_series = Series.objects.get(name='Theta')
    upsilon_series = Series.objects.get(name='Upsilon')

    beta_products = beta_series.products.all()
    theta_products = theta_series.products.all()
    upsilon_products = upsilon_series.products.all()

    context = {
        'title': 'Интернет-магазин компьютеров – Категория OPTIMAL',
        'beta_series': beta_series,
        'theta_series': theta_series,
        'upsilon_series': upsilon_series,
        'beta_products': beta_products,
        'theta_products': theta_products,
        'upsilon_products': upsilon_products,
    }
    return render(request, 'mcshop/pc_models_pages/optimal.html', context)


def powerful(request):
    alpha_series = Series.objects.get(name='Alpha')
    gamma_series = Series.objects.get(name='Gamma')
    delta_series = Series.objects.get(name='Delta')

    alpha_products = alpha_series.products.all()
    gamma_products = gamma_series.products.all()
    delta_products = delta_series.products.all()

    context = {
        'title': 'Интернет-магазин компьютеров – Категория POWERFUL',
        'alpha_series': alpha_series,
        'gamma_series': gamma_series,
        'delta_series': delta_series,
        'alpha_products': alpha_products,
        'gamma_products': gamma_products,
        'delta_products': delta_products,
    }
    return render(request, 'mcshop/pc_models_pages/powerful.html', context)


def alpha(request):
    products = Products.objects.all().filter(name__contains='Alpha')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия ALPHA',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/alpha.html', context)


def delta(request):
    products = Products.objects.all().filter(name__contains='Delta')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия DELTA',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/delta.html', context)


def gamma(request):
    products = Products.objects.all().filter(name__contains='Gamma')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия GAMMA',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/gamma.html', context)


def kappa(request):
    products = Products.objects.all().filter(name__contains='Kappa')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия KAPPA',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/kappa.html', context)


def lambda_page(request):
    products = Products.objects.all().filter(name__contains='Lambda')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия LAMBDA',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/lambda.html', context)


def omega(request):
    products = Products.objects.all().filter(name__contains='Omega')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия OMEGA',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/omega.html', context)


def omicron(request):
    products = Products.objects.all().filter(name__contains='Omicron')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия OMICRON',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/omicron.html', context)


def sigma(request):
    products = Products.objects.all().filter(name__contains='Sigma')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия SIGMA',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/sigma.html', context)


def theta(request):
    products = Products.objects.all().filter(name__contains='Theta')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия THETA',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/theta.html', context)


def zeta(request):
    products = Products.objects.all().filter(name__contains='Zeta')

    context = {
        'title': 'Интернет-магазин компьютеров – Серия ZETA',
        'products': products,
    }
    return render(request, 'mcshop/pc_series_pages/zeta.html', context)


def product_detail(request, product_slug):
    products = Products.objects.get(slug=product_slug)
    images = products.images.all()
    recommended = Products.objects.all().filter(price__gt=70000).filter(price__lt=90000).order_by('-price')

    context = {
        'title': 'Интернет-магазин компьютеров',
        'products': products,
        'images': images,
        'recomended': recommended
    }

    return render(request, 'mcshop/product_detail.html', context=context)


def cart(request):
    return render(request, 'mcshop/cart.html')


def checkout(request):
    return render(request, 'mcshop/checkout.html')


def configurator(request):
    return render(request, 'mcshop/configurator.html')
