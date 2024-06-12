from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True, null=True, verbose_name='Аватарка')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
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
