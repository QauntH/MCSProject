from django import template

from mcshop.utils import get_user_carts


register = template.Library()


@register.simple_tag()
def cart(request):
    return get_user_carts(request)
