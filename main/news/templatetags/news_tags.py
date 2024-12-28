from django import template
from news.models import Category

# Django simple tags
register = template.Library()

# you can use name paramatr to change function name
@register.simple_tag()
def get_all_categories():
    return Category.objects.all()