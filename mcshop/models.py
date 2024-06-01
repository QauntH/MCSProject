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


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='mcshop_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE,
                                 blank=True, null=True,verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'


class Optimal(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'optimal'
        verbose_name = 'Оптимальный'
        verbose_name_plural = 'Оптимальные'

    def __str__(self):
        return self.name


class Powerful(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'powerful'
        verbose_name = 'Мощный'
        verbose_name_plural = 'Мощные'

    def __str__(self):
        return self.name


class Custom(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'custom'
        verbose_name = 'Кастомный'
        verbose_name_plural = 'Кастомные'

    def __str__(self):
        return self.name


class Notebooks(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'notebook'
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

    def __str__(self):
        return self.name
