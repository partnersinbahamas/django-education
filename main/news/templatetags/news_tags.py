from django import template
from news.models import Category, Article
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Count, F
from django.core.cache import cache

# Django simple tags
register = template.Library()

# you can use name paramatr to change function name
# Simple tag uses to return values
@register.simple_tag()
def get_all_categories():
    categories = cache.get('categories')

    if not categories:
        categories = Category.objects.annotate(count=Count('categories', filter=F('categories__is_published'))).filter(count__gt=0)

    cache.set('categories', categories, 60)
      
    return categories

# Inclusion tag uses to return values an render the templates
@register.inclusion_tag('news/list_categories.html')
def show_all_categories(selected_category=None):
    categories = Category.objects.all()

    return {'categories': categories, 'selected_category': selected_category}


def get_article_by_id(article_id=None):
    # if object does not exist, it returns 404 error code
    # args1= your Model, where we need to get object, args2=id
    return get_object_or_404(Article, pk=article_id)

@register.simple_tag()
def get_category(category_id):
    return get_object_or_404(Category, pk=category_id)

@register.simple_tag()
def get_category_published_articles(category_id):
    get_category(category_id)
    return Article.objects.filter(category_id=category_id, is_published=True)
        