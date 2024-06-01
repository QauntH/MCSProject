# from django.db import models
# from mcshop.models import Product
# from django.contrib.auth.models import AbstractUser
#
#
# class User(AbstractUser):
#     phone_number = models.CharField(max_length=20, blank=True)
#     address = models.CharField(max_length=255, blank=True)
#
#     def __str__(self):
#         return self.username
#
#
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
#     products = models.ManyToManyField(Product, related_name='orders')
#     created_at = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=12, decimal_places=2)
#
#     def __str__(self):
#         return f'Заказ №{self.id} от {self.user.username} ({self.created_at})'
