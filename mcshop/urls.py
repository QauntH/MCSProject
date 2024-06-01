from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base_generic/', views.base_generic, name='base_generic'),
    path('products/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
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
    path('pay-delivery/', views.payment_delivery_info, name='pay'),
    path('configurator/', views.configurator, name='configurator'),
    path('support/', views.support, name='support'),
    path('custom/', views.custom, name='custom'),
    path('notebooks/', views.notebook, name='notebook'),
    path('optimal/', views.optimal, name='optimal'),
    path('powerful/', views.powerful, name='powerful'),
]
