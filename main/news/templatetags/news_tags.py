from django import template
from news.models import Category

# Django simple tags
register = template.Library()

# you can use name paramatr to change function name
# Simple tag uses to return values
@register.simple_tag()
def get_all_categories():
    return Category.objects.all()

# Inclusion tag uses to return values an render the templates
@register.inclusion_tag('news/list_categories.html')
def show_all_categories(selected_category=None):
    categories = Category.objects.all()

    return {'categories': categories, 'selected_category': selected_category}