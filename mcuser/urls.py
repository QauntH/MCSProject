from django.urls import path
from . import views

app_name = 'mcuser'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('pay-delivery/', views.payment_delivery_info, name='pay'),
    path('support/', views.support, name='support'),
    path('public_offer/', views.public_offer, name='public_offer'),
    path('copyright/', views.copyright_page, name='copyright'),
]
