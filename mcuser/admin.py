from django.contrib import admin
from mcuser.models import User
from mcshop.admin import CartTabAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'address', 'phone_number', 'email', ]
    search_fields = ['username', 'first_name', 'last_name', 'address', 'phone_number', 'email', ]

    inlines = [CartTabAdmin, ]
