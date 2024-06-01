from django.contrib import admin
from mcshop.models import *


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Optimal)
class OptimalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Powerful)
class PowerfulAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Custom)
class CustomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Notebooks)
class NotebooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
