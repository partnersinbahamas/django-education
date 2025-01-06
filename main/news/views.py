from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Article
from .templatetags.news_tags import get_all_categories, get_article_by_id, get_category_published_articles
from .form import ArticleForm
from django.views.generic import ListView

# Create your views here.

# def index(request):
#     news = Article.objects.order_by('-created_at')

#     data = {
#       'news': news,
#     }
#     return render(request, 'news/news.html', data)
# ----------

# same logic implemantation as def index() but with OOP
class HomeNewsList(ListView):
    """
    this will take all Article from Article model
    same as Article.objects.all()
    """

    model = Article
    # our template name, default is [app_name]_list.html: news_list.html
    template_name = 'news/news.html'
    # a variable name which we use on template: defautl is object_list
    context_object_name = 'news'
    
    """
    if we need to add some extra variables to template
    we can use extra_context dict, but only if is static data
    extra_context = {'page_name': 'page'}
    """
    # 
    """
    if our extra data is dinamic, use get_context_data func
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'page'
        return context
    
    # used to retrieve a set of data that will be passed to the template or used for further processing
    def get_queryset(self):
        return Article.objects.filter(is_published=True)


# def by_category(request, pk):
#     # pk came from url category/<int:pk> in urls
#     news = Article.objects.filter(category_id=pk)
#     # using simple tag
#     categories = get_all_categories()
#     selected_category = categories.get(id=pk)

#     data = {
#         'news': news,
#         'categories': categories,
#         'selected_category': selected_category,
#     }

#     return render(request, 'news/news.html', data)
# ----------
# same logic implemantation as def by_category() but with OOP
class NewsByCategory(ListView):
    model = Article
    template_name = 'news/news.html'
    context_object_name = 'news'
    # """
    # do not allow to show empty list
    # if category id will not found, is raise PageNotFound
    # """
    # allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = get_all_categories()
        # we take our pk from urls path using self.kwargs
        selected_category = categories.get(id=self.kwargs['pk'])

        context['categories'] = categories
        context['selected_category'] = selected_category

        return context
    
    def get_queryset(self):
        return get_category_published_articles(category_id=self.kwargs['pk'])

def view_article(request, article_id):
    article = get_article_by_id(article_id)

    data = {
        'article': article
    }

    return render(request, 'news/article.html', data)

def add_article(request):
    if request.method == 'POST':

        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            # in form.cleaned_data saves all fields which passed the validation
            # form.cleaned_data

            # if out model isnt binded with model we need to save it manualy
            # article = Article.objects.create(**form.cleaned_data)
            
            # we can use form.save() if our form binded with model used with ModelForm
            article = form.save()
            return redirect(article.get_absolute_url())
    else:
        form = ArticleForm()

    data = {
        'form': form,
    }

    return render(request, 'news/add_article.html', data)

