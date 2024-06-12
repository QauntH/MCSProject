from django.urls import path
from . import views

app_name = 'mcorders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
]