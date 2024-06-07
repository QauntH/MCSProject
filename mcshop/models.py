from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Серия')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        db_table = 'series'
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='product_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0, max_digits=8, decimal_places=0, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    graphic_card = models.TextField(blank=True, null=True, verbose_name='Графическая карта')
    processor = models.TextField(blank=True, null=True, verbose_name='Процессор')
    motherboard = models.TextField(blank=True, null=True, verbose_name='Материнская плата')
    ram = models.TextField(blank=True, null=True, verbose_name='Оперативная память')
    ssd = models.TextField(blank=True, null=True, verbose_name='SSD накопитель')
    power_unit = models.TextField(blank=True, null=True, verbose_name='Блок питания')
    pc_case = models.TextField(blank=True, null=True, verbose_name='Корпус')
    pc_os = models.TextField(blank=True, null=True, verbose_name='Операционная система')
    avg_fps = models.IntegerField(default=0, verbose_name='Средний FPS')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE,
                                 blank=True, null=True, verbose_name='Категория')
    series = models.ForeignKey(to=Series, related_name='products', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='Серия')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def display_id(self):
        return f'{self.id:04}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)

        return self.price


class ProductsImage(models.Model):
    product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', blank=True, null=True, verbose_name='Изображения')

    class Meta:
        db_table = 'product_image'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return f'Изображение: {self.product.name}'

# class PCModel(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(max_length=200, blank=True, null=True)
#     slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
#     category = models.ForeignKey(Categories, related_name='models', on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'model'
#         verbose_name = 'Модель'
#         verbose_name_plural = 'Модели'
#
#     def __str__(self):
#         return self.name
