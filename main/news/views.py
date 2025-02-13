from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Article
from .templatetags.news_tags import get_all_categories, get_category_published_articles
from .form import ArticleForm
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F
from .utils import TitleControl
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

# ORM

# Create your views here.

# def index(request):
#     news = Article.objects.order_by('-created_at')

#     data = {
#       'news': news,
#     }
#     return render(request, 'news/news.html', data)
# ----------

# same logic implemantation as def index() but with OOP
# ListView extend Paginator class
class HomeNewsList(TitleControl, ListView):
    """
    this will take all Article from Article model
    same as Article.objects.all()
    """

    model = Article
    # our template name, default is [app_name]_list.html: news_list.html
    template_name = 'news/news.html'
    # a variable name which we use on template: defautl is object_list
    context_object_name = 'news'
    m_prop = 'string in HomeNewsList class'
    # to paginate view list by
    paginate_by = 2

    """
        select relate here if we do not using get_queryset func
        queryset = Article.objects.select_related('category')
    """
    
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
        context['m_prop'] = self.get_prop_upper()
        context['title'] = self.get_upper('News')
        return context
    
    # used to retrieve a set of data that will be passed to the template or used for further processing
    """
        select_related method is used to optimize database queries by reducing the number of SQL queries executed when accessing related models. 
        using with ForeignKey model
    """
    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category')


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
class NewsByCategory(TitleControl, ListView):
    model = Article
    template_name = 'news/news.html'
    context_object_name = 'news'
    paginate_by = 2
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
        context['title'] = self.get_upper(selected_category, fieldName='name')

        return context
    
    def get_queryset(self):
        return get_category_published_articles(category_id=self.kwargs['pk']).select_related('category')

# def view_article(request, article_id):
#     article = get_article_by_id(article_id)

#     data = {
#         'article': article
#     }

#     return render(request, 'news/article.html', data)
    
# same logic implemantation as def view_article() but with OOP
class ArticleView(DetailView):
    model = Article
    """
      by default django search pk from Article
      but in urls we use article_id
      thats why we need to change the pk from urls to article_id
    """
    pk_url_kwarg = 'article_id'
    template_name = 'news/article.html'
    context_object_name = 'article'

    # here we can also use 
    """
      def get_context_data(self, **kwargs: Any):
      def get_queryset(self):
    """

    def get_object(self, queryset=None):
        article = super().get_object(queryset)

        Article.objects.filter(pk=article.pk).update(views=F('views') + 1)
        article.refresh_from_db(fields=['views'])

        return article


# def add_article(request):
#     if request.method == 'POST':

#         form = ArticleForm(request.POST, request.FILES)

#         if form.is_valid():
#             # in form.cleaned_data saves all fields which passed the validation
#             # form.cleaned_data

#             # if out model isnt binded with model we need to save it manualy
#             # article = Article.objects.create(**form.cleaned_data)
            
#             # we can use form.save() if our form binded with model used with ModelForm
#             article = form.save()
#             return redirect(article.get_absolute_url())
#     else:
#         form = ArticleForm()

#     data = {
#         'form': form,
#     }

#     return render(request, 'news/add_article.html', data)
    
# same logic implemantation as def add_article() but with OOP
# LoginRequiredMixin allow only for authenticaated users
class CreateArticle(LoginRequiredMixin, CreateView):
    # we need to bind our form with view using form_class
    # as model = Article in ListView, ...
    form_class = ArticleForm
    template_name = 'news/add_article.html'

    # redirec if user not loged
    login_url = '/admin'

    # throu an 403 Forbidden error if user no logged
    # raise_exception = True

    """
      if we didnt defin a get_absolute_url func
      we can redirect to after creation using:
      success_url = reverse_lazy('view_article')
    """

    # here we can also use 
    """
      def get_context_data(self, **kwargs: Any):
      def get_queryset(self):
    """


# test paginator class with functon
# def test_pagination(request):
#     objects = ['object-1', 'object-2', 'object-3', 'object-4', 'object-5', 'object-6', 'object-7', 'object-8',  'object-9']
#     paginatior = Paginator(objects, 2) # (objects, objects on page)
#     page = request.GET.get('page', 1)
#     pages = paginatior.get_page(page)

#     data = {
#         'page_obj': pages
#     }

#     return render(request, 'news/test_pagination.html', data)