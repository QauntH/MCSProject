from django.urls import path
from . import views

app_name = 'mcshop'

urlpatterns = [
    path('', views.home, name='home'),
    path('base_generic/', views.base_generic, name='base_generic'),
    path('products/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('beta/', views.beta, name='beta'),
    path('alpha/', views.alpha, name='alpha'),
    path('upsilon/', views.upsilon, name='upsilon'),
    path('delta/', views.delta, name='delta'),
    path('gamma/', views.gamma, name='gamma'),
    path('kappa/', views.kappa, name='kappa'),
    path('lambda/', views.lambda_page, name='lambda'),
    path('omega/', views.omega, name='omega'),
    path('omicron/', views.omicron, name='omicron'),
    path('sigma/', views.sigma, name='sigma'),
    path('theta/', views.theta, name='theta'),
    path('zeta/', views.zeta, name='zeta'),
    path('configurator/', views.configurator, name='configurator'),
    path('custom/', views.custom, name='custom'),
    path('notebooks/', views.notebook, name='notebook'),
    path('optimal/', views.optimal, name='optimal'),
    path('powerful/', views.powerful, name='powerful'),
    path('cart/', views.cart, name='cart'),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('cart_change/', views.cart_change, name='cart_change'),
    path('cart_remove/', views.cart_remove, name='cart_remove'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
]
