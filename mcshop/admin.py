from django.contrib import admin
from mcshop.models import *


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductsImageInline(admin.TabularInline):
    model = ProductsImage
    extra = 1


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductsImageInline]
    list_display = ['name', 'category', 'price', 'discount']
    list_editable = ['price', 'discount']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'category', 'series']
    fields = [
        'name',
        ('category', 'series'),
        ('price', 'discount'),
        'image',
        'description',
        'graphic_card',
        'processor',
        'motherboard',
        'ram',
        'ssd',
        'power_unit',
        'pc_case',
        'pc_os',
        'avg_fps',
        'slug',
    ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created_timestamp', 'session_key']
    search_fields = ['user', 'product', 'quantity', 'created_timestamp', 'session_key']
    list_filter = ['product', 'created_timestamp']
    fields = [
        'user',
        'product',
        'quantity',
        'created_timestamp',
        'session_key'
    ]


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'created_timestamp'
    search_fields = 'product', 'quantity', 'created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1
