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


admin.site.register(Cart)
